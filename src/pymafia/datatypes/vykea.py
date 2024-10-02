from __future__ import annotations

from dataclasses import dataclass, field
from functools import partial
from typing import TYPE_CHECKING, Any, ClassVar

from pymafia.kolmafia import km, on_kolmafia_start
from pymafia.lazy_enum import LazyEnum

if TYPE_CHECKING:
    from pymafia.datatypes.element import Element


class VykeaCompanionType(LazyEnum):
    NONE = partial(lambda: km.VYKEACompanionData.VYKEACompanionType.NONE)
    BOOKSHELF = partial(lambda: km.VYKEACompanionData.VYKEACompanionType.BOOKSHELF)
    DRESSER = partial(lambda: km.VYKEACompanionData.VYKEACompanionType.DRESSER)
    CEILING_FAN = partial(lambda: km.VYKEACompanionData.VYKEACompanionType.CEILING_FAN)
    COUCH = partial(lambda: km.VYKEACompanionData.VYKEACompanionType.COUCH)
    LAMP = partial(lambda: km.VYKEACompanionData.VYKEACompanionType.LAMP)
    DISHRACK = partial(lambda: km.VYKEACompanionData.VYKEACompanionType.DISHRACK)


class VykeaRune(LazyEnum):
    NONE = partial(lambda: km.VYKEACompanionData.NO_RUNE)
    FRENZY = partial(lambda: km.VYKEACompanionData.FRENZY_RUNE)
    BLOOD = partial(lambda: km.VYKEACompanionData.BLOOD_RUNE)
    LIGHTNING = partial(lambda: km.VYKEACompanionData.LIGHTNING_RUNE)


@dataclass(frozen=True, order=True)
class Vykea:
    NONE: ClassVar[Vykea]

    companion: Any = field(compare=False)
    type: VykeaCompanionType
    rune: VykeaRune
    level: int

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str)
            and key.casefold() == km.DataTypes.VYKEA_INIT.contentString.casefold()
        ) or key is None:
            object.__setattr__(self, "companion", self.default_companion)
            object.__setattr__(self, "type", self.default_type)
            object.__setattr__(self, "rune", self.default_rune)
            object.__setattr__(self, "level", self.default_level)
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
        from pymafia.ash import from_java

        values = km.DataTypes.VYKEA_TYPE.allValues()
        return from_java(values)

    @property
    def default_companion(self) -> Any:
        return km.VYKEACompanionData.NO_COMPANION

    @property
    def default_type(self) -> VykeaCompanionType:
        return VykeaCompanionType(self.default_companion.getType())

    @property
    def default_rune(self) -> VykeaRune:
        return VykeaRune(self.default_companion.getRune())

    @property
    def default_level(self) -> int:
        return self.default_companion.getLevel()

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


@on_kolmafia_start
def initialize_vykea_instances():
    Vykea.NONE = Vykea()
