"""
utils : "everything else".

"""

from .entity_register import entity_register

log = print


def unit_name_list(unit_list: list = []) -> list:
    return [unit.name for unit in unit_list]


def unit_type_from_name(unit_name=None):
    if unit_name is None:
        raise ValueError('cannot convert None to unit type')
    unl = unit_name_list(entity_register)
    lookup_table = dict(list(zip(unl, entity_register)))
    result = lookup_table[unit_name]
    return result


def unitstats(unit=None):
    if unit is None:
        raise ValueError('please provide a unit')
    if isinstance(unit, str):
        unit = unit_type_from_name(unit, entity_register)
    raise NotImplementedError('unitstats not implemented yet')


def f_sum(x, y):
    return x + y


