from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from ._stat import Stat


class Class:
    id: int = 0
    name: str = "none"
    ascension_class: Any = None

    def __init__(self, key: int | str | None = None):
        if key in (None, self.id, self.name):
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
        return hash((self.id, self.name))

    def __eq__(self, other) -> bool:
        return isinstance(other, type(self)) and (self.id, self.name) == (
            other.id,
            other.name,
        )

    def __bool__(self) -> bool:
        return (self.id, self.name) != (type(self).id, type(self).name)

    @classmethod
    def all(cls) -> list[Class]:
        from pymafia import ash

        values = km.DataTypes.CLASS_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def primestat(self) -> Stat:
        from ._stat import Stat

        if not self:
            return Stat.NONE
        prime_index = self.ascension_class.getPrimeStatIndex()
        name = km.AdventureResult.STAT_NAMES[prime_index]
        return Stat[name.upper()]
