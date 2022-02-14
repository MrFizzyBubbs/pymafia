import pymafia.kolmafia as km
from pymafia import ash, datatypes


class Class:
    id = -1
    name = "none"
    ascension_class = None

    def __init__(self, key=None):
        if key in (None, self.id, self.name):
            return

        ascension_class = km.AscensionClass.find(key)

        if ascension_class is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = ascension_class.getId()
        self.name = ascension_class.getName()
        self.ascension_class = ascension_class

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self):
        return hash((self.id, self.name))

    def __eq__(self, other):
        return isinstance(other, type(self)) and (self.id, self.name) == (
            other.id,
            other.name,
        )

    def __bool__(self):
        return (self.id, self.name) != (type(self).id, type(self).name)

    @classmethod
    def all(cls):
        values = km.DataTypes.CLASS_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def primestat(self):
        if not self:
            return datatypes.Stat.NONE
        prime_index = self.ascension_class.getPrimeStatIndex()
        stat_name = km.AdventureResult.STAT_NAMES[prime_index]
        return datatypes.Stat[stat_name.upper()]
