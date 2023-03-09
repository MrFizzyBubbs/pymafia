from __future__ import annotations

from functools import total_ordering
from typing import Any

from pymafia.kolmafia import km

MonsterDatabaseElement = getattr(km, "persistence.MonsterDatabase$Element")


@total_ordering
class Element:
    name: str = "none"
    element: Any = None

    def __init__(self, key: str | None = None):
        if key.casefold() == self.name.casefold() or key is None:
            return

        element = km.MonsterDatabase.stringToElement(key)
        if element == MonsterDatabaseElement.NONE:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.name = element.toString()
        self.element = element

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
    def all(cls) -> list[Element]:
        from pymafia import ash

        values = km.DataTypes.ELEMENT_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def image(self) -> str:
        # No image for Slime or Supercold in Manuel
        if self.element in [
            MonsterDatabaseElement.NONE,
            MonsterDatabaseElement.SLIME,
            MonsterDatabaseElement.SUPERCOLD,
        ]:
            return "circle.gif"
        if self.element == MonsterDatabaseElement.COLD:
            return "snowflake.gif"
        if self.element == MonsterDatabaseElement.HOT:
            return "fire.gif"
        if self.element == MonsterDatabaseElement.SLEAZE:
            return "wink.gif"
        if self.element == MonsterDatabaseElement.SPOOKY:
            return "skull.gif"
        if self.element == MonsterDatabaseElement.STENCH:
            return "stench.gif"
        return ""
