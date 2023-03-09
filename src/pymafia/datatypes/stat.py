from __future__ import annotations

from functools import total_ordering
from typing import Any

from pymafia.kolmafia import km


@total_ordering
class Stat:
    name: str = "none"

    def __init__(self, key: str | None = None):
        if key.casefold() == self.name.casefold() or key is None:
            return

        for stat in km.DataTypes.STAT_VALUES:
            name = stat.toString()
            if name.casefold() == key.casefold():
                self.name = name
                return

        raise ValueError(f"{type(self).__name__} {key!r} not found")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.name == other.name
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.name < other.name
        return NotImplemented

    def __bool__(self) -> bool:
        return self.name != type(self).name

    @classmethod
    def all(cls) -> list[Stat]:
        from pymafia import ash

        values = km.DataTypes.STAT_TYPE.allValues()
        return sorted(ash.to_python(values))
