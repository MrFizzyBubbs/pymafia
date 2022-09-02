import pymafia.kolmafia as km
from pymafia import ash


class Servant:
    id = 0
    name = "none"
    data = None

    def __init__(self, key):
        if key in (None, self.id, self.name):
            return

        data = (
            km.EdServantData.typeToData(key)
            if isinstance(key, str)
            else km.EdServantData.idToData(key)
        )

        if data is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = data[2]
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
        values = km.DataTypes.SERVANT_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def servant(self):
        return km.EdServantData.findEdServant(self.name)

    @property
    def level(self):
        return 0 if self.servant is None else self.servant.getLevel()

    @property
    def experience(self):
        return 0 if self.servant is None else self.servant.getExperience()

    @property
    def image(self):
        return self.data[3] if self else ""

    @property
    def level1_ability(self):
        return self.data[4] if self else ""

    @property
    def level7_ability(self):
        return self.data[5] if self else ""

    @property
    def level14_ability(self):
        return self.data[6] if self else ""

    @property
    def level21_ability(self):
        return self.data[7] if self else ""
