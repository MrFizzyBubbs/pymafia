from enum import IntEnum

import pymafia.kolmafia as km
from pymafia import ash


class EffectQuality(IntEnum):
    NONE = -1
    GOOD = 0
    NEUTRAL = 1
    BAD = 2


class Effect:
    id = -1
    name = "none"

    def __init__(self, key=None):
        if key in (None, self.id, self.name):
            return

        id_ = km.EffectDatabase.getEffectId(key) if isinstance(key, str) else key
        name = km.EffectDatabase.getEffectName(id_)

        if name is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = id_
        self.name = name

    def __str__(self):
        ids = km.EffectDatabase.getEffectIds(self.name, False)
        return f"[{self.id}]{self.name}" if len(ids) > 1 else self.name

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self):
        return hash((self.id, self.name))

    def __eq__(self, other):
        return isinstance(other, type(self)) and (self.id, self.name) == (
            other.id,
            other.name,
        )

    def __bool__(self):
        return (self.id, self.name) != (type(self).id, type(self).name)

    @classmethod
    def all(cls):
        values = km.DataTypes.EFFECT_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def default(self):
        return km.EffectDatabase.getDefaultAction(self.id) or ""

    @property
    def quality(self):
        return EffectQuality(km.EffectDatabase.getQuality(self.id))

    @property
    def attributes(self):
        attrs = km.EffectDatabase.getEffectAttributes(self.id)
        return [] if attrs is None else list(attrs)

    @property
    def actions(self):
        return list(km.EffectDatabase.getAllActions(self.id))

    @property
    def note(self):
        return km.EffectDatabase.getActionNote(self.id) or ""

    @property
    def image(self):
        return km.EffectDatabase.getImageName(self.id)

    @property
    def descid(self):
        return km.EffectDatabase.getDescriptionId(self.id) or ""

    @property
    def candy_tier(self):
        return km.CandyDatabase.getEffectTier(self.id)
