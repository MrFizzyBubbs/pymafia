from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.element import Element


class VykeaCompanionType(Enum):
    NONE = km.VYKEACompanionData.VYKEACompanionType.NONE
    BOOKSHELF = km.VYKEACompanionData.VYKEACompanionType.BOOKSHELF
    DRESSER = km.VYKEACompanionData.VYKEACompanionType.DRESSER
    CEILING_FAN = km.VYKEACompanionData.VYKEACompanionType.CEILING_FAN
    COUCH = km.VYKEACompanionData.VYKEACompanionType.COUCH
    LAMP = km.VYKEACompanionData.VYKEACompanionType.LAMP
    DISHRACK = km.VYKEACompanionData.VYKEACompanionType.DISHRACK


class VykeaRune(Enum):
    NONE = km.VYKEACompanionData.NO_RUNE
    FRENZY = km.VYKEACompanionData.FRENZY_RUNE
    BLOOD = km.VYKEACompanionData.BLOOD_RUNE
    LIGHTNING = km.VYKEACompanionData.LIGHTNING_RUNE


@dataclass(frozen=True, order=True)
class Vykea:
    NONE: ClassVar[Vykea]

    companion: Any = field(default=km.VYKEACompanionData.NO_COMPANION, compare=False)
    type: VykeaCompanionType = VykeaCompanionType(companion.default.getType())
    rune: VykeaRune = VykeaRune(companion.default.getRune())
    level: int = companion.default.getLevel()

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str)
            and key.casefold() == km.DataTypes.VYKEA_INIT.contentString.casefold()
        ) or key is None:
            return

        companion = km.VYKEACompanionData.fromString(key)
        if companion is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "companion", companion)
        object.__setattr__(self, "type", VykeaCompanionType(companion.getType()))
        object.__setattr__(self, "rune", VykeaRune(companion.getRune()))
        object.__setattr__(self, "level", companion.getLevel())

    def __str__(self) -> str:
        return (
            self.companion.toString() if self else km.DataTypes.VYKEA_INIT.contentString
        )

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Vykea]:
        from pymafia.ash.conversion import from_java

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
        from pymafia.datatypes.element import Element

        return Element(self.companion.getAttackElement().toString())


Vykea.NONE = Vykea()
