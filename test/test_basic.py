import faf
from faf import *


def test_basic():
    assert 1 == 1
    print("test_basic passed.")


def test_unit_type_from_name():
    assert isinstance(faf.utils.unit_type_from_name('Com'), Com)


def test_can_endgame_be_built():
    current_unit_list = list()
    current_unit_list.append(Com())

    for idx in range(8):
        current_unit_list.append(MexPlace())

    assert (Endgame.can_be_built(faf.utils.unit_name_list(current_unit_list)) is False)
    current_unit_list.append(Mavor())
    assert (Endgame.can_be_built(faf.utils.unit_name_list(current_unit_list)) is True)
