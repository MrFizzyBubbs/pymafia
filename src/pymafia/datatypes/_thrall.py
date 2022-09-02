import pymafia.kolmafia as km
from pymafia import ash, datatypes


class Thrall:
    id = 0
    name = "none"
    data = None

    def __init__(self, key=None):
        if key in (None, self.id, self.name):
            return

        data = (
            km.PastaThrallData.typeToData(key)
            if isinstance(key, str)
            else km.PastaThrallData.idToData(key)
        )

        if data is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = data[1]
        self.name = data[0]
        self.data = data

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
        values = km.DataTypes.THRALL_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def thrall(self):
        return km.KoLCharacter.findPastaThrall(self.name)

    @property
    def level(self):
        return self.thrall.getLevel() if self else 0

    @property
    def image(self):
        return self.data[6] if self else ""

    @property
    def tinyimage(self):
        return self.data[7] if self else ""

    @property
    def skill(self):
        return datatypes.Skill(self.data[3]) if self else None

    @property
    def current_modifiers(self):
        return self.thrall.getCurrentModifiers() if self else ""
