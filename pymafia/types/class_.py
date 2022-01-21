from pymafia.kolmafia import km
from pymafia import ash


class Class:
    def __init__(self, key):
        if key in (None, -1, "none"):
            self.id = -1
            self.name = "none"
            return

        ascension_class = (
            km.AscensionClass.nameToClass(key)
            if isinstance(key, str)
            else km.AscensionClass.idToClass(int(key))
        )

        if ascension_class is None:
            raise NameError(f"{type(self).__name__} {key!r} not found")

        self.id = ascension_class.getId()
        self.name = ascension_class.getName()

    @classmethod
    def all(cls):
        values = km.DataTypes.CLASS_TYPE.allValues()
        return sorted(ash.from_java(values), key=lambda x: x.id)

    def __hash__(self):
        return hash((self.id, self.name))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __eq__(self, other):
        return isinstance(other, type(self)) and (self.id, self.name) == (
            other.id,
            other.name,
        )

    def __bool__(self):
        return self.name != "none"
