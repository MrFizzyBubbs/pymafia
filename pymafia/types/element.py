from enum import Enum


class Element(Enum):
    NONE = "none"
    COLD = "cold"
    HOT = "hot"
    SLEAZE = "sleaze"
    SPOOKY = "spooky"
    STENCH = "stench"
    SLIME = "slime"
    SUPERCOLD = "supercold"

    def __str__(self):
        return self.value

    def __bool__(self):
        return self.value != "none"

    @classmethod
    def _missing_(cls, value):
        if value is None:
            return cls.NONE
        return super()._missing_(value)

    @classmethod
    def all(cls):
        return list(cls)
