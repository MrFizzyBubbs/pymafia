from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING, Any

import pymafia.kolmafia as km

if TYPE_CHECKING:
    from ._element import Element
    from ._item import Item


class VykeaType(IntEnum):
    NONE = km.VYKEACompanionData.NONE
    BOOKSHELF = km.VYKEACompanionData.BOOKSHELF
    DRESSER = km.VYKEACompanionData.DRESSER
    CEILING_FAN = km.VYKEACompanionData.CEILING_FAN
    COUCH = km.VYKEACompanionData.COUCH
    LAMP = km.VYKEACompanionData.LAMP
    DISHRACK = km.VYKEACompanionData.DISHRACK


class Vykea:
    companion: Any = km.VYKEACompanionData.NO_COMPANION

    def __init__(self, key: str | None = None):
        if key in (None, "none"):
            return

        companion = km.VYKEACompanionData.fromString(key)
        if companion is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.companion = companion

    def __str__(self) -> str:
        return self.companion.toString()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self) -> int:
        return hash((self.type_, self.rune, self.level))

    def __eq__(self, other) -> bool:
        return isinstance(other, type(self)) and (
            self.type_,
            self.rune,
            self.level,
        ) == (other.type_, other.rune, other.level)

    def __bool__(self) -> bool:
        return self.companion != type(self).companion

    @classmethod
    def all(cls) -> list[Vykea]:
        from pymafia import ash

        values = km.DataTypes.VYKEA_TYPE.allValues()
        return ash.to_python(values)

    @property
    def name(self) -> str:
        return self.companion.getName()

    @property
    def type_(self) -> VykeaType:
        return VykeaType(self.companion.getType())

    @property
    def rune(self) -> Item:
        return Item(self.companion.getRune().getItemId())

    @property
    def level(self) -> int:
        return self.companion.getLevel()

    @property
    def image(self) -> str:
        return self.companion.getImage()

    @property
    def modifiers(self) -> str:
        return self.companion.getModifiers()

    @property
    def attack_element(self) -> Element:
        return Element(self.companion.getAttackElement().toString())
