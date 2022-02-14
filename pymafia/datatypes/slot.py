from enum import Enum


class Slot(Enum):
    NONE = "none"
    HAT = "hat"
    WEAPON = "weapon"
    HOLSTER = "holster"
    OFFHAND = "off-hand"
    BACK = "back"
    SHIRT = "shirt"
    PANTS = "pants"
    ACC1 = "acc1"
    ACC2 = "acc2"
    ACC3 = "acc3"
    FAMILIAR = "familiar"
    CROWNOFTHRONES = "crown-of-thrones"
    STICKER1 = "sticker1"
    STICKER2 = "sticker2"
    STICKER3 = "sticker3"
    CARDSLEEVE = "card-sleeve"
    FOLDER1 = "folder1"
    FOLDER2 = "folder2"
    FOLDER3 = "folder3"
    FOLDER4 = "folder4"
    FOLDER5 = "folder5"
    BUDDYBJORN = "buddy-bjorn"
    BOOTSKIN = "bootskin"
    BOOTSPUR = "bootspur"
    FAKEHAND = "fakehand"

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
