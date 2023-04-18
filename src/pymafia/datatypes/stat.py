from __future__ import annotations

from dataclasses import dataclass

from pymafia.kolmafia import km


@dataclass(frozen=True, order=True)
class Stat:
    name: str = km.DataTypes.STAT_INIT.contentString

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.name.casefold()
        ) or key is None:
            return

        for stat in km.DataTypes.STAT_VALUES:
            name = stat.toString()
            if name.casefold() == key.casefold():
                object.__setattr__(self, "name", name)
                return

        raise ValueError(f"{type(self).__name__} {key!r} not found")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Stat]:
        from pymafia.ash import from_java

        values = km.DataTypes.STAT_TYPE.allValues()
        return from_java(values)
