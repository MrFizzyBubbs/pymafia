from enum import Enum

import pymafia.kolmafia as km


class Phylum(Enum):
    NONE = "none"
    BEAST = "beast"
    BUG = "bug"
    CONSTELLATION = "constellation"
    CONSTRUCT = "construct"
    DEMON = "demon"
    DUDE = "dude"
    ELEMENTAL = "elemental"
    ELF = "elf"
    FISH = "fish"
    GOBLIN = "goblin"
    HIPPY = "hippy"
    HOBO = "hobo"
    HORROR = "horror"
    HUMANOID = "humanoid"
    MER_KIN = "mer-kin"
    ORC = "orc"
    PENGUIN = "penguin"
    PIRATE = "pirate"
    PLANT = "plant"
    SLIME = "slime"
    UNDEAD = "undead"
    WEIRD = "weird"

    def __str__(self):
        return self.value

    def __bool__(self):
        return self is not self.NONE

    @classmethod
    def _missing_(cls, value):
        if value is None:
            return cls.NONE
        return super()._missing_(value)

    @classmethod
    def all(cls):
        return list(cls)

    @property
    def image(self):
        phylum = km.autoclass(
            "net/sourceforge/kolmafia/persistence/MonsterDatabase$Phylum"
        ).find(self.value)
        if type(self)(phylum.toString()) is self.NONE:
            return ""
        return phylum.getImage()
