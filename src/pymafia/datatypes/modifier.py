from __future__ import annotations

from dataclasses import dataclass, field
from functools import partial
from typing import Any, ClassVar

from pymafia.kolmafia.kolmafia import on_kolmafia_start

from pymafia.kolmafia import km
from pymafia.lazy_enum import LazyEnum


class ModifierValueType(LazyEnum):
    NONE = partial(lambda: km.ModifierValueType.NONE)
    NUMERIC = partial(lambda: km.ModifierValueType.NUMERIC)
    BOOLEAN = partial(lambda: km.ModifierValueType.BOOLEAN)
    STRING = partial(lambda: km.ModifierValueType.STRING)


@dataclass(frozen=True, order=True)
class Modifier:
    NONE: ClassVar[Modifier]

    modifier: Any = field(compare=False)
    name: str

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.default_name.casefold()
        ) or key is None:
            object.__setattr__(self, "modifier", self.default_modifier)
            object.__setattr__(self, "name", self.default_name)
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
        from pymafia.ash import from_java

        values = km.DataTypes.MODIFIER_TYPE.allValues()
        return from_java(values)

    @property
    def default_modifier(self) -> Any:
        return km.DataTypes.MODIFIER_INIT.content

    @property
    def default_name(self) -> str:
        return km.DataTypes.MODIFIER_INIT.contentString

    @property
    def type_(self) -> ModifierValueType:
        modifier_value_type = (
            self.modifier.getType()
            if self.modifier is not None
            else km.ModifierValueType.NONE
        )
        return ModifierValueType(modifier_value_type)


@on_kolmafia_start
def initialize_modifier_instances():
    Modifier.NONE = Modifier()
