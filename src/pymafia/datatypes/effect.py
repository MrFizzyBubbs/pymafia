from __future__ import annotations

from enum import IntEnum
from functools import total_ordering
from typing import Any

from pymafia.kolmafia import km


class EffectQuality(IntEnum):
    NONE = -1
    GOOD = 0
    NEUTRAL = 1
    BAD = 2


@total_ordering
class Effect:
    id: int = -1
    name: str = "none"

    def __init__(self, key: int | str | None = None):
        if key in (None, self.name, self.id):
            return

        id = km.EffectDatabase.getEffectId(key) if isinstance(key, str) else key
        name = km.EffectDatabase.getEffectName(id)
        if name is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = id
        self.name = name

    def __str__(self) -> str:
        ids = km.EffectDatabase.getEffectIds(self.name, False)
        return f"[{self.id}]{self.name}" if len(ids) > 1 else self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id == other.id
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id < other.id
        return NotImplemented

    def __bool__(self) -> bool:
        return self.id != type(self).id

    @classmethod
    def all(cls) -> list[Effect]:
        from pymafia import ash

        values = km.DataTypes.EFFECT_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def default(self) -> str:
        return km.EffectDatabase.getDefaultAction(self.id) or ""

    @property
    def actions(self) -> list[str]:
        return list(km.EffectDatabase.getAllActions(self.id))

    @property
    def quality(self) -> EffectQuality:
        return EffectQuality(km.EffectDatabase.getQuality(self.id))

    @property
    def attributes(self) -> list[str]:
        attrs = km.EffectDatabase.getEffectAttributes(self.id)
        return [] if attrs is None else list(attrs)

    @property
    def note(self) -> str:
        return km.EffectDatabase.getActionNote(self.id) or ""

    @property
    def image(self) -> str:
        return km.EffectDatabase.getImageName(self.id)

    @property
    def descid(self) -> str:
        return km.EffectDatabase.getDescriptionId(self.id) or ""

    @property
    def candy_tier(self) -> int:
        return km.CandyDatabase.getEffectTier(self.id)

    @property
    def song(self) -> bool:
        return km.EffectDatabase.isSong(self.id)
