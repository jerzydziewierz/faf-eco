from .entities_base import BaseEntity, remove_from_list

log = print

class LandFactoryT1(BaseEntity):
    name = "LandFactoryT1"
    cost_buildpower = 300.0
    cost_mass = 240.0
    cost_energy = 2100
    provides_buildpower = 0.0
    provides_mass = 0.0
    provides_energy = 00.0
    landunit_buildpower = 20.0

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        exists = set(unit_list)
        to_build_require = {'Com'}
        can_build = to_build_require.intersection(exists) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list: list) -> list:
        unit_list.append(LandFactoryT1())
        return unit_list


class EngineerT1(BaseEntity):
    name = "EngineerT1"
    cost_buildpower = 260.0
    cost_mass = 52.0
    cost_energy = 260
    provides_buildpower = 5.0
    provides_mass = 0.0
    provides_energy = 00.0
    mass_storage = 10.0
    landunit_buildpower = 0.0

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        exists = set(unit_list)
        to_build_require = {'LandFactoryT1'}
        can_build = to_build_require.intersection(exists) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list: list) -> list:
        unit_list.append(EngineerT1())
        return unit_list


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
