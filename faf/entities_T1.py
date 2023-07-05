from .entities_base import BaseEntity, remove_from_list

log = print


class PowerplantT1(BaseEntity):
    name = "PowerplantT1"
    cost_buildpower = 125.0
    cost_mass = 75.0
    cost_energy = 750
    provides_buildpower = 0.0
    provides_mass = 0.0
    provides_energy = 20.0

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        exists = set(unit_list)
        to_build_require = {'Com'}
        can_build = to_build_require.intersection(exists) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list: list) -> list:
        unit_list.append(PowerplantT1())
        return unit_list


class MexT1(BaseEntity):
    name = "MexT1"
    cost_buildpower = 60
    cost_mass = 36
    cost_energy = 360
    provides_buildpower = 0.0
    provides_mass = 2.0
    provides_energy = -2.0

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        exists_in_available = set(unit_list)
        to_build_require = {'Com', 'MexPlace'}
        # this verifies that all the items that are required, exist in the unit list
        can_build = to_build_require.intersection(exists_in_available) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list: list) -> list:
        new_list = remove_from_list(unit_list, item_to_remove="MexPlace")
        new_list.append(MexT1())
        return new_list
