from .entities_base import BaseEntity

log = print


class Mavor(BaseEntity):
    cost_buildpower = 300000.0
    cost_mass = 224775.0
    cost_energy = 5.994e6
    name = "Mavor"

    def __init__(self):
        super().__init__()

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        exists = set(unit_list)
        to_build_require = {['Com']}
        can_build = to_build_require.intersection(exists) == to_build_require
        return can_build

    @staticmethod
    def on_build(unit_list: list) -> list:
        unit_list.append(Mavor())
        return unit_list
