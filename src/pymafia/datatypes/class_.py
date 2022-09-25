from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from .stat import Stat


@total_ordering
class Class:
    id: int = 0
    name: str = "none"
    ascension_class: Any = None

    def __init__(self, key: int | str | None = None):
        if key in (None, self.name, self.id):
            return

        ascension_class = km.AscensionClass.find(key)
        if ascension_class is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = ascension_class.getId()
        self.name = ascension_class.getName()
        self.ascension_class = ascension_class

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id == other.id
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id < other.id
        return NotImplemented

    def __bool__(self) -> bool:
        return self.id != type(self).id

    @classmethod
    def all(cls) -> list[Class]:
        from pymafia import ash

        values = km.DataTypes.CLASS_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def primestat(self) -> Stat:
        from .stat import Stat

        if not self:
            return Stat.NONE
        prime_index = self.ascension_class.getPrimeStatIndex()
        name = km.AdventureResult.STAT_NAMES[prime_index]
        return Stat[name.upper()]
