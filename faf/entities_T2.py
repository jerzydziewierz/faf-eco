from typing import List, Any

from .entities_base import BaseEntity, remove_from_list

log = print


class MexT2(BaseEntity):
    name: str = "MexT2"
    cost_buildpower: float = 1171.0
    cost_mass: float = 900.0
    cost_energy: float = 5400.0
    provides_buildpower: float = 0.0
    provides_mass: float = 6.0
    provides_energy: float = -9.0

    @staticmethod
    def name():
        return MexT2().name

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        exists_in_available = set(unit_list)
        to_build_require = {['MexT1']}
        # this verifies that all the items that are required, exist in the unit list
        can_build = to_build_require.intersection(exists_in_available) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list: list) -> list:
        filtered_list = remove_from_list(unit_list, item_to_remove="MexT1")
        filtered_list.append(MexT2())
        return filtered_list
