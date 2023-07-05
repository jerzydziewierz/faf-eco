from faf import *
from faf.build_selector1 import buildorder_simple1
import copy


def main():
    gs = init_game_state()
    gs_history = []

    for idx in range(300000):
        # note that the build selector is adjustable because this is the primary thing that we will be optimizing.
        gs, is_game_over = game_step(gs, build_selector=buildorder_simple1)
        gs_history.append(copy.copy(gs))
        if is_game_over:
            break
        if gs.log_worthy:
            log(f'cycle {gs.idx_gamecycle} : building {gs.currently_building} ({gs.currently_building_buildpower_progress:0.0f} @ {gs.eco.actual_bp_usable:0.0f} : {gs.build_cycles_remaining_estimate:0.0f} steps),  PC={gs.energy_production_capability:0.0f}/{gs.mass_production_capability:0.0f}/{gs.build_power_capability:0.0f}, bank = {gs.energy_bank:0.0f}/{gs.mass_bank:0.0f}')

    for key in gs.keys():
        print(f'{key} : {gs[key]}')

    print(f'game over in {gs.idx_gamecycle} steps.')
    # reference run length: 111098 steps. if we can get any better,that's better.


if __name__ == "__main__":
    main()
