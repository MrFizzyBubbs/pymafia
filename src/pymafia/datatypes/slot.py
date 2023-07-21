from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from pymafia.kolmafia import km


@dataclass(frozen=True, order=True)
class Slot:
    NONE: ClassVar[Slot]
    HAT: ClassVar[Slot]
    WEAPON: ClassVar[Slot]
    HOLSTER: ClassVar[Slot]
    OFFHAND: ClassVar[Slot]
    BACK: ClassVar[Slot]
    SHIRT: ClassVar[Slot]
    PANTS: ClassVar[Slot]
    ACC1: ClassVar[Slot]
    ACC2: ClassVar[Slot]
    ACC3: ClassVar[Slot]
    FAMILIAR: ClassVar[Slot]
    CROWNOFTHRONES: ClassVar[Slot]
    STICKER1: ClassVar[Slot]
    STICKER2: ClassVar[Slot]
    STICKER3: ClassVar[Slot]
    CARDSLEEVE: ClassVar[Slot]
    FOLDER1: ClassVar[Slot]
    FOLDER2: ClassVar[Slot]
    FOLDER3: ClassVar[Slot]
    FOLDER4: ClassVar[Slot]
    FOLDER5: ClassVar[Slot]
    BUDDYBJORN: ClassVar[Slot]
    BOOTSKIN: ClassVar[Slot]
    BOOTSPUR: ClassVar[Slot]
    FAKEHAND: ClassVar[Slot]

    name: str = km.DataTypes.SLOT_INIT.contentString

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.name.casefold()
        ) or key is None:
            return

        slot = km.EquipmentRequest.slotNumber(key)
        if slot == km.Slot.NONE:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "name", slot.name)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Slot]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.SLOT_TYPE.allValues()
        return from_java(values)


Slot.NONE = Slot()
Slot.HAT = Slot("hat")
Slot.WEAPON = Slot("weapon")
Slot.HOLSTER = Slot("holster")
Slot.OFFHAND = Slot("off-hand")
Slot.BACK = Slot("back")
Slot.SHIRT = Slot("shirt")
Slot.PANTS = Slot("pants")
Slot.ACC1 = Slot("acc1")
Slot.ACC2 = Slot("acc2")
Slot.ACC3 = Slot("acc3")
Slot.FAMILIAR = Slot("familiar")
Slot.CROWNOFTHRONES = Slot("crown-of-thrones")
Slot.STICKER1 = Slot("sticker1")
Slot.STICKER2 = Slot("sticker2")
Slot.STICKER3 = Slot("sticker3")
Slot.CARDSLEEVE = Slot("card-sleeve")
Slot.FOLDER1 = Slot("folder1")
Slot.FOLDER2 = Slot("folder2")
Slot.FOLDER3 = Slot("folder3")
Slot.FOLDER4 = Slot("folder4")
Slot.FOLDER5 = Slot("folder5")
Slot.BUDDYBJORN = Slot("buddy-bjorn")
Slot.BOOTSKIN = Slot("bootskin")
Slot.BOOTSPUR = Slot("bootspur")
Slot.FAKEHAND = Slot("fakehand")
