from faf import *
from faf import Com
from faf.utils import f_sum
from functools import reduce
from mict import mict

def init_game_state():
    game_state = mict()
    game_state.current_unit_list = list()
    game_state.idx_gamecycle = 0
    # init bank.

    game_state.energy_bank = 0.0
    game_state.mass_bank = 0.0
    game_state.energy_wasted_accumulator = 0.0
    game_state.mass_wasted_accumulator = 0.0

    # add a Com. Game starts with a Com.

    game_state.current_unit_list.append(Com())
    # add 8 mex places - this simulates "dual gap" map.
    for idx in range(8):
        game_state.current_unit_list.append(MexPlace())

    # at first, nothing is building.
    game_state.currently_building = None
    game_state.currently_building_buildpower_progress = 0.0

    # the game starts with "full bank". Although, I observe that in the real game, the starting energy is 4000, not just Com's 3600.
    # I am not sure where does this discrepancy come from, maybe the ground itself can store 400 energy?
    # I will add a special unit "ground" that will store 400 energy and 0 mass.
    game_state.current_unit_list.append(SpecialGround())

    # game initializes with full bank:
    game_state.mass_bank = reduce(f_sum, [unit.mass_storage for unit in game_state.current_unit_list])
    game_state.energy_bank = reduce(f_sum, [unit.energy_storage for unit in game_state.current_unit_list])
    return game_state
