from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, ClassVar

from pymafia.kolmafia import km


class ModifierValueType(Enum):
    NONE = km.ModifierValueType.NONE
    NUMERIC = km.ModifierValueType.NUMERIC
    BOOLEAN = km.ModifierValueType.BOOLEAN
    STRING = km.ModifierValueType.STRING


@dataclass(frozen=True, order=True)
class Modifier:
    NONE: ClassVar[Modifier]

    modifier: Any = field(default=km.DataTypes.MODIFIER_INIT.content, compare=False)
    name: str = km.DataTypes.MODIFIER_INIT.contentString

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.name.casefold()
        ) or key is None:
            return

        modifier = km.ModifierDatabase.byCaselessName(key)
        if modifier is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "modifier", modifier)
        object.__setattr__(self, "name", modifier.getName())

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Modifier]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.MODIFIER_TYPE.allValues()
        return from_java(values)

    @property
    def type_(self) -> ModifierValueType:
        modifier_value_type = (
            self.modifier.getType()
            if self.modifier is not None
            else km.ModifierValueType.NONE
        )
        return ModifierValueType(modifier_value_type)


Modifier.NONE = Modifier()
