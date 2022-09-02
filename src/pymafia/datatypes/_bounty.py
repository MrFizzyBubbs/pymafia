import pymafia.kolmafia as km
from pymafia import ash, datatypes


class Bounty:
    name = "none"

    def __init__(self, key=None):
        if key in (None, self.name):
            return

        bounties = km.BountyDatabase.getMatchingNames(key)

        if len(bounties) != 1:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        canonical = bounties[0]
        self.name = km.BountyDatabase.canonicalToName(canonical)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.name == other.name

    def __bool__(self):
        return self.name != type(self).name

    @classmethod
    def all(cls):
        values = km.DataTypes.BOUNTY_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.name)

    @property
    def plural(self):
        return km.BountyDatabase.getPlural(self.name) or ""

    @property
    def type_(self):
        return km.BountyDatabase.getType(self.name) or ""

    @property
    def kol_internal_type(self):
        if self.type_ == "easy":
            return "low"
        if self.type_ == "hard":
            return "high"
        return None

    @property
    def number(self):
        return km.BountyDatabase.getNumber(self.name)

    @property
    def image(self):
        return km.BountyDatabase.getImage(self.name) or ""

    @property
    def monster(self):
        return datatypes.Monster(km.BountyDatabase.getMonster(self.name)) or None

    @property
    def location(self):
        return datatypes.Location(km.BountyDatabase.getLocation(self.name)) or None
