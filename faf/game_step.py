from functools import reduce

from faf import Endgame
from faf.utils import f_sum
import numpy
from mict import mict
from faf.build_selector1 import buildorder_simple1
from faf.build_selector1 import apply_next_build_order


def game_step(
        game_state,
        build_selector=buildorder_simple1,
        log=print,
        step_callback=None):
    is_game_over = False
    # "gs" = "game_state"
    gs = game_state
    gs.log_worthy = False
    gs.idx_gamecycle += 1
    # add energy and mass to the bank, up to the capacity
    gs.mass_production_capability = reduce(f_sum, [unit.provides_mass for unit in gs.current_unit_list])
    gs.energy_production_capability = reduce(f_sum, [unit.provides_energy for unit in gs.current_unit_list])
    gs.build_power_capability = reduce(f_sum, [unit.provides_buildpower for unit in gs.current_unit_list])

    gs.mass_storage_capacity = reduce(f_sum, [unit.mass_storage for unit in gs.current_unit_list])
    gs.energy_storage_capacity = reduce(f_sum, [unit.energy_storage for unit in gs.current_unit_list])

    gs.mass_bank = gs.mass_bank + gs.mass_production_capability
    gs.mass_wasted_this_step = numpy.maximum(0, game_state.mass_bank - gs.mass_storage_capacity);
    gs.mass_wasted_accumulator += gs.mass_wasted_this_step
    gs.mass_bank = numpy.minimum(gs.mass_storage_capacity, gs.mass_bank)

    gs.energy_bank = gs.energy_bank + gs.energy_production_capability
    gs.energy_wasted_this_step = numpy.maximum(0.0, gs.energy_bank - gs.energy_storage_capacity)
    gs.energy_wasted_accumulator += gs.energy_wasted_this_step

    gs.energy_bank = numpy.minimum(gs.energy_storage_capacity, game_state.energy_bank)

    gs.energy_overflow = gs.energy_wasted_this_step > 0.0
    gs.mass_overflow = gs.mass_wasted_this_step > 0.0

    # if not building, select new thing to build:
    if gs.currently_building is None:
        next_unit = build_selector(gs)
        if isinstance(next_unit, Endgame):
            is_game_over = True
            return gs, is_game_over
        gs = apply_next_build_order(gs, next_unit)
        gs.log_worthy = True

    # approach:
    # given current build power, energy_bank, mass_bank
    # how much build power can be spent?
    # note that this does not come from the game's source code, but rather, is my recreation according to the observations.
    # it appears to function correctly.
    eco = mict()
    eco.mass_per_bp = gs.currently_building.cost_mass / gs.currently_building.cost_buildpower
    eco.energy_per_bp = gs.currently_building.cost_energy / gs.currently_building.cost_buildpower

    eco.mass_spend_proposal = gs.build_power_capability * eco.mass_per_bp
    eco.energy_spend_proposal = gs.build_power_capability * eco.energy_per_bp

    eco.bank_limited_mass_spend = numpy.minimum(eco.mass_spend_proposal, gs.mass_bank)
    eco.bank_limited_energy_spend = numpy.minimum(eco.energy_spend_proposal, gs.energy_bank)

    eco.bp_mass_spend_limited = eco.bank_limited_mass_spend / eco.mass_per_bp
    eco.bp_energy_spend_limited = eco.bank_limited_energy_spend / eco.energy_per_bp

    eco.actual_bp_usable = numpy.minimum(eco.bp_mass_spend_limited, eco.bp_energy_spend_limited)

    eco.actual_mass_used = eco.actual_bp_usable * eco.mass_per_bp
    eco.actual_energy_used = eco.actual_bp_usable * eco.energy_per_bp

    # apply
    gs.currently_building_buildpower_progress += eco.actual_bp_usable
    gs.mass_bank -= eco.actual_mass_used
    gs.energy_bank -= eco.actual_energy_used

    # note underflow, if any
    gs.mass_underflow = gs.mass_bank < 1.0
    gs.energy_underflow = gs.energy_bank < 1.0
    # build underflow is when the actual mass used is approximately equal to the mass spend proposal, and the same for energy.
    gs.build_underflow = numpy.abs(eco.actual_mass_used - eco.mass_spend_proposal) < 1.0 and \
                         numpy.abs(eco.actual_energy_used - eco.energy_spend_proposal) < 1.0

    # compute build potential: given the current mass and energy production, how much build power can be used?
    gs.build_power_usage_potential_by_mass = gs.mass_production_capability * eco.mass_per_bp
    gs.build_power_usage_potential_by_energy = gs.energy_production_capability * eco.energy_per_bp
    gs.build_power_usage_potential = numpy.minimum(gs.build_power_usage_potential_by_mass, gs.build_power_usage_potential_by_energy)


    # save calculations for post-run analysis
    gs.eco = eco

    # if build finished:
    if gs.currently_building_buildpower_progress > gs.currently_building.cost_buildpower:
        # Modify the unit list as per effects of this unit being built
        gs.current_unit_list = gs.currently_building.on_build(gs.current_unit_list)
        # remove the unit from the build queue
        gs.currently_building_buildpower_progress = 0.0
        gs.currently_building = None
        gs.build_cycles_remaining_estimate = numpy.nan
    else:
        gs.build_cycles_remaining_estimate = \
            (gs.currently_building.cost_buildpower -
             gs.currently_building_buildpower_progress) / eco.actual_bp_usable

    if (gs.idx_gamecycle % 10000 == 0) and gs.currently_building is not None:
        gs.log_worthy = True

    return game_state, is_game_over
