from __future__ import annotations

from typing import TYPE_CHECKING

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from ._location import Location
    from ._monster import Monster


class Bounty:
    name: str = "none"

    def __init__(self, key: int | str | None = None):
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

    def __eq__(self, other) -> bool:
        return isinstance(other, type(self)) and self.name == other.name

    def __bool__(self) -> bool:
        return self.name != type(self).name

    @classmethod
    def all(cls) -> list[Bounty]:
        from pymafia import ash

        values = km.DataTypes.BOUNTY_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.name)

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
        from ._monster import Monster

        return Monster(km.BountyDatabase.getMonster(self.name))

    @property
    def location(self) -> Location:
        from ._location import Location

        return Location(km.BountyDatabase.getLocation(self.name))
