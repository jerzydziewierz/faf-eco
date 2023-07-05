from typing import Any
from warnings import warn
from attrs import frozen


@frozen
class BaseEntity:
    """
    base entity from which all other entities are derived.
    The concept is to simplify the interfaces by always using class instances, rather than types.

    Hence, units should not really have state; properties are const, and methods are static.
    """
    name = "BaseEntity"
    cost_buildpower = 0.0
    cost_mass = 0.0
    cost_energy = 0.0
    provides_buildpower = 0.0
    provides_mass = 0.0
    provides_energy = 0.0
    mass_storage = 0.0
    energy_storage = 0.0

    @staticmethod
    def name():
        """
        must return the class name as a string.
        this is to be used as a key in the entity dictionary.
        :return: string name.
        """
        return "BaseEntity"

    @staticmethod
    def can_be_built(unit_list: list) -> bool:
        """
    Takes a list of current units available, and returns True if this can be built.
    e.g. a T1 land factory can be built if there is a commander.
    a T2 land factory can be built if there is a T1 land factory, e.t.c.

    """
        warn("can_be_built() not implemented for this entity.")
        return False

    @staticmethod
    def on_build(unit_list: list) -> list:
        """
    when build is complete, takes a list of current units, and returns an updated list.
    For example, a unit can be created, converted, or consumed.
    """
        warn("on_build() not implemented for this entity.")
        return unit_list

    @classmethod
    def __str__(cls):
        return f'{cls().name}'

    def __call__(self, *args, **kwargs):
        return self.name


def remove_from_list(unit_list: list, item_to_remove: str) -> list:
    """
    removes one instance of this entity from the list, and returns the updated list.
    """
    is_first_item: bool = True
    filtered_list: list[Any] = [item for item in unit_list if
                                not (item.name == item_to_remove and is_first_item)
                                or (is_first_item := False)]
    return filtered_list
