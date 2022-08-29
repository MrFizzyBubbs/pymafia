from enum import IntEnum

import pymafia.kolmafia as km
from pymafia import ash, datatypes


class VykeaType(IntEnum):
    NONE = km.VYKEACompanionData.NONE
    BOOKSHELF = km.VYKEACompanionData.BOOKSHELF
    DRESSER = km.VYKEACompanionData.DRESSER
    CEILING_FAN = km.VYKEACompanionData.CEILING_FAN
    COUCH = km.VYKEACompanionData.COUCH
    LAMP = km.VYKEACompanionData.LAMP
    DISHRACK = km.VYKEACompanionData.DISHRACK


class Vykea:
    companion = km.VYKEACompanionData.NO_COMPANION

    def __init__(self, key=None):
        if key in (None, "none"):
            return

        companion = km.VYKEACompanionData.fromString(key)

        if companion is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.companion = companion

    def __str__(self):
        return self.companion.toString()

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self):
        return hash((self.type_, self.rune, self.level))

    def __eq__(self, other):
        return isinstance(other, type(self)) and (
            self.type_,
            self.rune,
            self.level,
        ) == (other.type_, other.rune, other.level)

    def __bool__(self):
        return self.companion != type(self).companion

    @classmethod
    def all(cls):
        values = km.DataTypes.VYKEA_TYPE.allValues()
        return ash.to_python(values)

    @property
    def name(self):
        return self.companion.getName()

    @property
    def type_(self):
        return VykeaType(self.companion.getType())

    @property
    def rune(self):
        item_id = self.companion.getRune().getItemId()
        return None if item_id == datatypes.Item.id else datatypes.Item(item_id)

    @property
    def level(self):
        return self.companion.getLevel()

    @property
    def image(self):
        return self.companion.getImage()

    @property
    def modifiers(self):
        return self.companion.getModifiers()

    @property
    def attack_element(self):
        return datatypes.Element(self.companion.getAttackElement().toString())
