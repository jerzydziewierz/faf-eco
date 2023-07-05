from .entities_base import BaseEntity, remove_from_list

log = print


class MexT3(BaseEntity):
    name = "MexT3"
    cost_buildpower = 3944
    cost_mass = 4600
    cost_energy = 31625
    provides_mass = 18.0
    provides_energy = -54.0

    @staticmethod
    def name():
        return "MexT3"

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        exists_in_available = set(unit_list)
        to_build_require = {['MexT2']}
        # this verifies that all the items that are required, exist in the unit list
        can_build = to_build_require.intersection(exists_in_available) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list: list) -> list:
        # remove one MexT1 from the list
        is_first_mex: bool = True
        new_list = remove_from_list(unit_list, item_to_remove="MexT2")
        new_list.append(MexT3())
        return new_list
