from pymafia.kolmafia import km
from pymafia.types import Item
from pymafia import ash


class Vykea:
    def __init__(self, key):
        if key in (None, "none"):
            self.type = "unknown"
            self.level = 0
            self.rune = Item(None)
            self.name = ""
            return

        companion = km.VYKEACompanionData.fromString(key)

        if companion is None:
            raise NameError(f"{type(self).__name__} {key!r} not found")

        self.type = companion.typeToString()
        self.level = companion.getLevel()
        self.rune = Item(companion.getRune().getItemId())
        self.name = companion.getName()

    @classmethod
    def all(cls):
        values = km.DataTypes.VYKEA_TYPE.allValues()
        return ash.from_java(values)

    def __hash__(self):
        return hash((self.type, self.level, self.rune))

    def __str__(self):
        if not self:
            return "none"

        s = ""
        if self.name:
            s += f"{self.name}, the "
        s += f"level {self.level} "
        if self.rune:
            rune = km.AdventureResult(km.AdventureResult.ITEM_PRIORITY, self.rune.name)
            s += km.VYKEACompanionData.runeToString(rune)
            s += " "
        s += self.type
        return s

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __eq__(self, other):
        return isinstance(other, type(self)) and (self.type, self.level, self.rune) == (
            other.type,
            other.level,
            other.rune,
        )

    def __bool__(self):
        return self.type != "unknown"
