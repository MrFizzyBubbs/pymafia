from __future__ import annotations

from enum import Enum
from typing import Any

from pymafia.kolmafia import km


class Zodiac(Enum):
    NONE = 0
    MONGOOSE = 1
    WALLABY = 2
    VOLE = 3
    PLATYPUS = 4
    OPOSSUM = 5
    MARMOT = 6
    WOMBAT = 7
    BLENDER = 8
    PACKRAT = 9
    BAD_MOON = 10

    def __str__(self) -> str:
        return self.name_

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.value < other.value
        return NotImplemented

    def __bool__(self) -> bool:
        return self is not self.NONE

    @classmethod
    def _missing_(cls, value) -> Zodiac:
        if value is None:
            return cls.NONE
        return super()._missing_(value)

    @classmethod
    def all(cls) -> list[Zodiac]:
        return list(cls)

    @property
    def sign(self) -> Any:
        return km.ZodiacSign.find(self.name)

    @property
    def name_(self) -> str:
        return self.sign.getName()

    @property
    def type_(self) -> str:
        return self.sign.getType().toString()

    @property
    def zone(self) -> str:
        return self.sign.getZone().toString()
