from enum import Enum


class Stat(Enum):
    NONE = "none"
    MUSCLE = "Muscle"
    MYSTICALITY = "Mysticality"
    MOXIE = "Moxie"
    SUBMUSCLE = "SubMuscle"
    SUBMYSTICALITY = "SubMysticality"
    SUBMOXIE = "SubMoxie"

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
