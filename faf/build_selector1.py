from mict import mict
from faf import *
from faf.utils import unit_name_list


def apply_next_build_order(game_state: mict = mict(), unit_to_build: BaseEntity = Com()) -> mict:
    """
    apply the next buildorder to the game state. This is to allow inspection of the build order generator before it is applied.
    :param game_state: game state.
    :param unit_to_build: Which unit to begin building (instance of unit derived from BaseEntity)
    :return:
    """
    game_state.currently_building = unit_to_build
    game_state.currently_building_buildpower_progress = 0
    return game_state


def buildorder_simple1(gs: mict = mict()):
    """
    :param gs: Game State. Mict.
    :return: selected unit (new instance)
    """
    # this will need to be a bit smart
    # for now, I will use an algorithmic approach
    # if we can build endgame, do it
    # if we can build a mex on a MexPlace, do it
    # then,
    # if there is less T1 powerplants than mexes of any kind, build T1 powerplant
    # then,
    # build mavor

    # if the end can be done, then do it
    if Endgame.can_be_built(unit_name_list(gs.current_unit_list)):
        return Endgame()

    # First step is to build land factory, it's just how all the builds work
    # let's say that we will only ever want one land factory T1
    if not 'LandFactoryT1' in unit_name_list(gs.current_unit_list):
        return LandFactoryT1()

    if MexT1.can_be_built(unit_name_list(gs.current_unit_list)):
        if gs.energy_production_capability > 8:  # but do not build if there is not enough power.
            return MexT1()

    if gs.energy_production_capability < 200:
        return PowerplantT1()

    return Mavor()

    # at this point, something must be selected.
    raise RuntimeError("No unit selected. This should not happen.")
