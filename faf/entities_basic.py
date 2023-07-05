from .entities_base import BaseEntity
log = print


class Com(BaseEntity):

    name = "Com"
    cost_buildpower = 0.0
    cost_mass = 0.0
    cost_energy = 0.0
    provides_buildpower = 10.0
    provides_mass = 1.0
    provides_energy = 10.0
    mass_storage = 650
    energy_storage = 3900

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        return False

    @staticmethod
    def on_build(unit_list: list) -> list:
        raise AssertionError("Cannot build a commander during the game.")


class Endgame(BaseEntity):
    name = "Endgame"
    cost_buildpower = 1.0

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        exists = set(unit_list)
        # ! potentially, this could be parametrized in the constructor to allow different scenarios.
        # for now, this is fixed to "mavor" as the endgame unit.
        to_build_require = set(['Mavor'])
        can_build = to_build_require.intersection(exists) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list: list) -> list:
        unit_list.append(Endgame())
        log('game ended.')
        return unit_list


class MexPlace(BaseEntity):
    name = "MexPlace"

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        exists = set(unit_list)
        to_build_require = set()
        can_build = to_build_require.intersection(exists) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list: list) -> list:
        raise AssertionError("Cannot build a MexPlace during the game.")


class SpecialGround(BaseEntity):
    """
    This is a special aux unit that stores 400 energy so that the starting energy is more in line with what the game shows.
    """

    name = "SpecialGround"

    mass_storage = 0
    energy_storage = 0

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        False

    @staticmethod
    def on_build(unit_list=[]) -> list:
        raise AssertionError("Cannot build a SpecialGround during the game.")