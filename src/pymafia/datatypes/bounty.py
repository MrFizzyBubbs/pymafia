from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from .location import Location
    from .monster import Monster


@total_ordering
class Bounty:
    name: str = "none"

    def __init__(self, key: str | None = None):
        if key in (None, self.name):
            return

        bounties = km.BountyDatabase.getMatchingNames(key)
        if len(bounties) != 1:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        canonical = bounties[0]
        self.name = km.BountyDatabase.canonicalToName(canonical)

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
    def all(cls) -> list[Bounty]:
        from pymafia import ash

        values = km.DataTypes.BOUNTY_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def plural(self) -> str:
        return km.BountyDatabase.getPlural(self.name) or ""

    @property
    def type_(self) -> str:
        return km.BountyDatabase.getType(self.name) or ""

    @property
    def kol_internal_type(self) -> str | None:
        match self.type_:
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
