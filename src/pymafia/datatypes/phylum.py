from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from pymafia.kolmafia import km


@dataclass(frozen=True, order=True)
class Phylum:
    NONE: ClassVar[Phylum]
    BEAST: ClassVar[Phylum]
    BUG: ClassVar[Phylum]
    CONSTELLATION: ClassVar[Phylum]
    CONSTRUCT: ClassVar[Phylum]
    DEMON: ClassVar[Phylum]
    DUDE: ClassVar[Phylum]
    ELEMENTAL: ClassVar[Phylum]
    ELF: ClassVar[Phylum]
    FISH: ClassVar[Phylum]
    GOBLIN: ClassVar[Phylum]
    HIPPY: ClassVar[Phylum]
    HOBO: ClassVar[Phylum]
    HORROR: ClassVar[Phylum]
    HUMANOID: ClassVar[Phylum]
    MERKIN: ClassVar[Phylum]
    ORC: ClassVar[Phylum]
    PENGUIN: ClassVar[Phylum]
    PIRATE: ClassVar[Phylum]
    PLANT: ClassVar[Phylum]
    SLIME: ClassVar[Phylum]
    UNDEAD: ClassVar[Phylum]
    WEIRD: ClassVar[Phylum]

    phylum: Any = field(default=km.DataTypes.PHYLUM_INIT.content, compare=False)
    name: str = km.DataTypes.PHYLUM_INIT.contentString

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.name.casefold()
        ) or key is None:
            return

        phylum = km.MonsterDatabase.Phylum.find(key)
        if phylum == km.MonsterDatabase.Phylum.NONE:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "phylum", phylum)
        object.__setattr__(self, "name", phylum.toString())

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Phylum]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.PHYLUM_TYPE.allValues()
        return sorted(from_java(values))

    @property
    def image(self) -> str:
        if self.phylum == km.MonsterDatabase.Phylum.NONE:
            return ""
        return self.phylum.getImage()


Phylum.NONE = Phylum()
Phylum.BEAST = Phylum("beast")
Phylum.BUG = Phylum("bug")
Phylum.CONSTELLATION = Phylum("constellation")
Phylum.CONSTRUCT = Phylum("construct")
Phylum.DEMON = Phylum("demon")
Phylum.DUDE = Phylum("dude")
Phylum.ELEMENTAL = Phylum("elemental")
Phylum.ELF = Phylum("elf")
Phylum.FISH = Phylum("fish")
Phylum.GOBLIN = Phylum("goblin")
Phylum.HIPPY = Phylum("hippy")
Phylum.HOBO = Phylum("hobo")
Phylum.HORROR = Phylum("horror")
Phylum.HUMANOID = Phylum("humanoid")
Phylum.MERKIN = Phylum("mer-kin")
Phylum.ORC = Phylum("orc")
Phylum.PENGUIN = Phylum("penguin")
Phylum.PIRATE = Phylum("pirate")
Phylum.PLANT = Phylum("plant")
Phylum.SLIME = Phylum("slime")
Phylum.UNDEAD = Phylum("undead")
Phylum.WEIRD = Phylum("weird")
