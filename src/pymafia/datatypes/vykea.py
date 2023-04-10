from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from .element import Element


@dataclass(frozen=True, order=True)
class Vykea:
    companion: Any = field(default=km.VYKEACompanionData.NO_COMPANION, compare=False)
    type: str = companion.default.typeToString()
    rune: str = companion.default.runeToString()
    level: int = companion.default.getLevel()

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == "none".casefold()
        ) or key is None:
            return

        companion = km.VYKEACompanionData.fromString(key)
        if companion is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "companion", companion)
        object.__setattr__(self, "type", companion.typeToString())
        object.__setattr__(self, "rune", companion.runeToString())
        object.__setattr__(self, "level", companion.getLevel())

    def __str__(self) -> str:
        return self.companion.toString() if self else "none"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self.companion != type(self).companion

    @classmethod
    def all(cls) -> list[Vykea]:
        from pymafia.conversion import from_java

        values = km.DataTypes.VYKEA_TYPE.allValues()
        return from_java(values)

    @property
    def name(self) -> str:
        return self.companion.getName()

    @property
    def image(self) -> str:
        return self.companion.getImage()

    @property
    def modifiers(self) -> str:
        return self.companion.getModifiers()

    @property
    def attack_element(self) -> Element:
        from .element import Element

        return Element(self.companion.getAttackElement().toString())
