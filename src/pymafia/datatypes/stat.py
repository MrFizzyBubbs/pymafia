from __future__ import annotations

from enum import Enum
from typing import Any


class Stat(Enum):
    NONE = "none"
    MUSCLE = "Muscle"
    MYSTICALITY = "Mysticality"
    MOXIE = "Moxie"
    SUBMUSCLE = "SubMuscle"
    SUBMYSTICALITY = "SubMysticality"
    SUBMOXIE = "SubMoxie"

    def __str__(self) -> str:
        return self.value

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.value < other.value
        return NotImplemented

    def __bool__(self) -> bool:
        return self is not self.NONE

    @classmethod
    def _missing_(cls, value) -> Stat:
        if value is None:
            return cls.NONE
        return super()._missing_(value)

    @classmethod
    def all(cls) -> list[Stat]:
        return list(cls)
