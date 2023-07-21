from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, ClassVar

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.location import Location
    from pymafia.datatypes.monster import Monster


class BountyType(Enum):
    NONE = None
    EASY = "easy"
    HARD = "hard"
    SPECIAL = "special"


class KoLInternalBountyType(Enum):
    NONE = BountyType.NONE
    LOW = BountyType.EASY
    HIGH = BountyType.HARD
    SPECIAL = BountyType.SPECIAL


@dataclass(frozen=True, order=True)
class Bounty:
    NONE: ClassVar[Bounty]

    name: str = km.DataTypes.BOUNTY_INIT.contentString

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
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Bounty]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.BOUNTY_TYPE.allValues()
        return from_java(values)

    @property
    def plural(self) -> str:
        return km.BountyDatabase.getPlural(self.name) or ""

    @property
    def type(self) -> BountyType:
        return BountyType(km.BountyDatabase.getType(self.name))

    @property
    def kol_internal_type(self) -> KoLInternalBountyType:
        return KoLInternalBountyType(self.type)

    @property
    def number(self) -> int:
        return km.BountyDatabase.getNumber(self.name)

    @property
    def image(self) -> str:
        return km.BountyDatabase.getImage(self.name) or ""

    @property
    def monster(self) -> Monster:
        from pymafia.datatypes.monster import Monster

        return Monster(km.BountyDatabase.getMonster(self.name))

    @property
    def location(self) -> Location:
        from pymafia.datatypes.location import Location

        return Location(km.BountyDatabase.getLocation(self.name))


Bounty.NONE = Bounty()
