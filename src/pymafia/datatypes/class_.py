from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.stat import Stat


@dataclass(frozen=True, order=True)
class Class:
    id: int = -1
    name: str = "none"

    def __init__(self, key: int | str | None = None):
        if (isinstance(key, str) and key.casefold() == self.name.casefold()) or key in (
            self.id,
            None,
        ):
            return

        ascension_class = km.AscensionClass.find(key)
        if ascension_class is None or ascension_class.getId() < 0:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "id", ascension_class.getId())
        object.__setattr__(self, "name", ascension_class.getName())

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return (self.id, self.name) != (type(self).id, type(self).name)

    @classmethod
    def all(cls) -> list[Class]:
        from pymafia.ash import from_java

        values = km.DataTypes.CLASS_TYPE.allValues()
        return sorted(from_java(values))

    @property
    def ascension_class(self) -> Any:
        return km.AscensionClass.find(self.id)

    @property
    def primestat(self) -> Stat:
        from pymafia.datatypes.stat import Stat

        if not self:
            return Stat(None)
        prime_index = self.ascension_class.getPrimeStatIndex()
        name = km.AdventureResult.STAT_NAMES[prime_index]
        return Stat(name)
