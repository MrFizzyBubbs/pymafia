from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from .location import Location
    from .monster import Monster


@dataclass(frozen=True, order=True)
class Bounty:
    name: str = "none"

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.name.casefold()
        ) or key is None:
            return

        bounties = km.BountyDatabase.getMatchingNames(key)
        if len(bounties) != 1:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        canonical = bounties[0]
        object.__setattr__(self, "name", km.BountyDatabase.canonicalToName(canonical))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self.name != type(self).name

    @classmethod
    def all(cls) -> list[Bounty]:
        from pymafia.conversion import from_java

        values = km.DataTypes.BOUNTY_TYPE.allValues()
        return from_java(values)

    @property
    def plural(self) -> str:
        return km.BountyDatabase.getPlural(self.name) or ""

    @property
    def type(self) -> str:
        return km.BountyDatabase.getType(self.name) or ""

    @property
    def kol_internal_type(self) -> str | None:
        match self.type:
            case "easy":
                return "low"
            case "hard":
                return "high"
            case "special":
                return "special"
            case _:
                return None

    @property
    def number(self) -> int:
        return km.BountyDatabase.getNumber(self.name)

    @property
    def image(self) -> str:
        return km.BountyDatabase.getImage(self.name) or ""

    @property
    def monster(self) -> Monster:
        from .monster import Monster

        return Monster(km.BountyDatabase.getMonster(self.name))

    @property
    def location(self) -> Location:
        from .location import Location

        return Location(km.BountyDatabase.getLocation(self.name))
