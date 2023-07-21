from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, ClassVar

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.stat import Stat


@dataclass(frozen=True, order=True)
class Class:
    NONE: ClassVar[Class]

    ascension_class: Any = field(default=km.DataTypes.CLASS_INIT.content, compare=False)
    id: int = km.DataTypes.CLASS_INIT.contentLong
    name: str = km.DataTypes.CLASS_INIT.contentString

    def __init__(self, key: int | str | None = None):
        if (isinstance(key, str) and key.casefold() == self.name.casefold()) or key in (
            self.id,
            None,
        ):
            return

        ascension_class = km.AscensionClass.find(key)
        if ascension_class is None or ascension_class.getId() < 0:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "ascension_class", ascension_class)
        object.__setattr__(self, "id", ascension_class.getId())
        object.__setattr__(self, "name", ascension_class.getName())

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Class]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.CLASS_TYPE.allValues()
        return sorted(from_java(values))

    @property
    def primestat(self) -> Stat:
        from pymafia.datatypes.stat import Stat

        if self.ascension_class is None:
            return Stat()
        prime_index = self.ascension_class.getPrimeStatIndex()
        name = km.AdventureResult.STAT_NAMES[prime_index]
        return Stat(name)


Class.NONE = Class()
