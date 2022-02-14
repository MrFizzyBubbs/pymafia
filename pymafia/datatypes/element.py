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
        if self is self.NONE:
            return "circle.gif"
        if self is self.COLD:
            return "snowflake.gif"
        if self is self.HOT:
            return "fire.gif"
        if self is self.SLEAZE:
            return "wink.gif"
        if self is self.SPOOKY:
            return "skull.gif"
        if self is self.STENCH:
            return "stench.gif"
        # No image for Slime or Supercold in Manuel
        if self is self.SLIME:
            return "circle.gif"
        if self is self.SUPERCOLD:
            return "circle.gif"
        return ""
