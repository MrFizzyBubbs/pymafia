from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import ClassVar

from pymafia.kolmafia import km


class EffectQuality(IntEnum):
    NONE = -1
    GOOD = 0
    NEUTRAL = 1
    BAD = 2


@dataclass(frozen=True, order=True)
class Effect:
    NONE: ClassVar[Effect]

    id: int = km.DataTypes.EFFECT_INIT.contentLong
    name: str = km.DataTypes.EFFECT_INIT.contentString

    def __init__(self, key: int | str | None = None):
        if (isinstance(key, str) and key.casefold() == self.name.casefold()) or key in (
            self.id,
            None,
        ):
            return

        id = km.EffectDatabase.getEffectId(key) if isinstance(key, str) else key
        name = km.EffectDatabase.getEffectName(id)
        if name is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "id", id)
        object.__setattr__(self, "name", name)

    def __str__(self) -> str:
        ids = km.EffectDatabase.getEffectIds(self.name, False)
        return f"[{self.id}]{self.name}" if len(ids) > 1 else self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Effect]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.EFFECT_TYPE.allValues()
        return sorted(from_java(values))

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
        return list(attrs) if attrs is not None else []

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


Effect.NONE = Effect()
