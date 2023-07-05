from .utils import log
from .entities_base import BaseEntity


class Com(BaseEntity):

    @staticmethod
    def name():
        return "com"

    def __init__(self):
        super().__init__()
        self.cost_buildpower = 0.0
        self.cost_mass = 0.0
        self.cost_energy = 0.0
        self.provides_buildpower = 10.0
        self.provides_mass = 1.0
        self.provides_energy = 10.0
        self.mass_storage = 650
        self.energy_storage = 3900

    @staticmethod
    def can_be_built(unit_list=[]) -> bool:
        return False

    @staticmethod
    def on_build(unit_list=[]) -> list:
        raise AssertionError("Cannot build a commander during the game.")


class Endgame(BaseEntity):

    @staticmethod
    def name():
        return "endgame"

    def __init__(self):
        super().__init__()
        self.cost_buildpower = 1.0
        self.cost_mass = 0.0
        self.cost_energy = 0.0
        self.provides_buildpower = 0.0
        self.provides_mass = 0.0
        self.provides_energy = 00.0

    @staticmethod
    def can_be_built(unit_list=[]) -> bool:
        exists = set(unit_list)
        # ! potentially, this could be parametrized in the constructor to allow different scenarios.
        # for now, this is fixed to "mavor" as the endgame unit.
        to_build_require = {'mavor'}
        can_build = to_build_require.intersection(exists) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list=[]) -> list:
        unit_list.append(Endgame())
        log('game ended.')
        return unit_list


class MexPlace(BaseEntity):

    @staticmethod
    def name():
        return "mexplace"

    def __init__(self):
        super().__init__()
        self.cost_buildpower = 0.0
        self.cost_mass = 0.0
        self.cost_energy = 0.0
        self.provides_buildpower = 0.0
        self.provides_mass = 0.0
        self.provides_energy = 00.0

    @staticmethod
    def can_be_built(unit_list=[]) -> bool:
        exists = set(unit_list)
        to_build_require = {}
        can_build = to_build_require.intersection(exists) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list=[]) -> list:
        raise AssertionError("Cannot build a mexplace during the game.")


class Mavor(BaseEntity):
    @staticmethod
    def name():
        return "mavor"

    def __init__(self):
        super().__init__()
        self.cost_buildpower = 300000.0
        self.cost_mass = 224775.0
        self.cost_energy = 5.994e6
        self.provides_buildpower = 0.0
        self.provides_mass = 0.0
        self.provides_energy = 00.0

    @staticmethod
    def can_be_built(unit_list=[]) -> bool:
        exists = set(unit_list)
        to_build_require = {'com'}
        can_build = to_build_require.intersection(exists) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list=[]) -> list:
        unit_list.append(Mavor())
        return unit_list


class PowerplantT1(BaseEntity):
    @staticmethod
    def name():
        return "powerplantT1"

    def __init__(self):
        super().__init__()
        self.cost_buildpower = 125.0
        self.cost_mass = 75.0
        self.cost_energy = 750
        self.provides_buildpower = 0.0
        self.provides_mass = 0.0
        self.provides_energy = 20.0

    @staticmethod
    def can_be_built(unit_list=[]) -> bool:
        exists = set(unit_list)
        to_build_require = {'com'}
        can_build = to_build_require.intersection(exists) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list=[]) -> list:
        unit_list.append(PowerplantT1())
        return unit_list


class MexT1(BaseEntity):
    @staticmethod
    def name():
        return "mexT1"

    def __init__(self):
        super().__init__()
        self.cost_buildpower = 60
        self.cost_mass = 36
        self.cost_energy = 360
        self.provides_buildpower = 0.0
        self.provides_mass = 2.0
        self.provides_energy = -2.0

    @staticmethod
    def can_be_built(unit_list=[]) -> bool:
        exists_in_available = set(unit_list)
        to_build_require = {'com', 'mexplace'}
        # this verifies that all the items that are required, exist in the unit list
        can_build = to_build_require.intersection(exists_in_available) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list=[]) -> list:
        # remove one mexplace from the list
        is_first_mexplace = True
        filtered_list = [item for item in unit_list if
                         not (item.name() == 'mexplace' and is_first_mexplace) or (is_first_mexplace := False)]
        # add one mexT1 to the list
        filtered_list.append(MexT1())
        return filtered_list
