
class BaseEntity:
    """
    base entity from which all other entities are derived.
    The concept is to simplify the interfaces by always using class instances, rather than types.

    Hence, units should not really have state; properties are const, and methods are static.
    """
    def __init__(self):
        self.cost_buildpower = None
        self.cost_mass = None
        self.cost_energy = None
        self.provides_buildpower = 0
        self.provides_mass = 0
        self.provides_energy = 0
        self.mass_storage = 0
        self.energy_storage = 0

    @staticmethod
    def name():
        """
        must return a lowercase unique string name for the entity, e.g. "landfactory"
        this is to be used as a key in the entity dictionary.
        :return: string name.
        """
        return "baseentity"

    @staticmethod
    def can_be_built() -> bool:
        """
    Takes a list of current units available, and returns True if this can be built.
    e.g. a T1 land factory can be built if there is a commander.
    a T2 land factory can be built if there is a T1 land factory, e.t.c.

    """
        return False

    @staticmethod
    def on_build(unit_list=[]) -> list:
        """
    when build is complete, takes a list of current units, and returns an updated list.
    For example, a unit can be created, converted, or consumed.
    """
        pass

    @classmethod
    def __str__(cls):
        return f'{cls.name()}'

    @classmethod
    def __repr__(cls):
        return f'{cls.name()}'

    @staticmethod
    def __call__(self, *args, **kwargs):
        return self.name()

    def __eq__(self, other):
        return self.name() == other.name()

    def __hash__(self):
        return hash(self.name())

    def __lt__(self, other):
        assert AssertionError("Cannot compare entities")

    def __gt__(self, other):
        assert AssertionError("Cannot compare entities")
