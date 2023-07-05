from faf import *
from faf.build_selector1 import *


def test_select_next_buildorder():

    # test 1: check if mavor is correctly selected
    observed_next = buildorder_simple1(
        gs=mict(current_unit_list=[], energy_production_capability=30000),
                    )
    assert (str(observed_next) == "Mavor")

    # test 2: check if powerplant is correctly selected
    observed_next = buildorder_simple1(
        gs=mict(
            current_unit_list=[],
            energy_production_capability=30),
                    )
    assert (str(observed_next) == "PowerplantT1")


    # test 3: check if Endgame is correctly selected
    observed_next = buildorder_simple1(
        gs=mict(current_unit_list=[Mavor()],
                        energy_production_capability=30000
                        )
                    )
    assert (str(observed_next) == "Endgame")


