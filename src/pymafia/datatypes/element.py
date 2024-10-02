from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from pymafia.kolmafia import km, on_kolmafia_start


@dataclass(frozen=True, order=True)
class Element:
    NONE: ClassVar[Element]
    COLD: ClassVar[Element]
    HOT: ClassVar[Element]
    SLEAZE: ClassVar[Element]
    SPOOKY: ClassVar[Element]
    STENCH: ClassVar[Element]
    SLIME: ClassVar[Element]
    SUPERCOLD: ClassVar[Element]
    BADSPELLING: ClassVar[Element]
    SHADOW: ClassVar[Element]

    element: Any = field(compare=False)
    name: str

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.default_name.casefold()
        ) or key is None:
            object.__setattr__(self, "element", self.default_element)
            object.__setattr__(self, "name", self.default_name)
            return

        element = km.MonsterDatabase.stringToElement(key)
        if element == km.MonsterDatabase.Element.NONE:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "element", element)
        object.__setattr__(self, "name", element.toString())

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Element]:
        from pymafia.ash import from_java

        values = km.DataTypes.ELEMENT_TYPE.allValues()
        return from_java(values)

    @property
    def default_element(self) -> Any:
        return km.DataTypes.ELEMENT_INIT.content

    @property
    def default_name(self) -> str:
        return km.DataTypes.ELEMENT_INIT.contentString

    @property
    def image(self) -> str:
        # No image for Slime or Supercold in Manuel
        if self.element in [
            km.MonsterDatabase.Element.NONE,
            km.MonsterDatabase.Element.SLIME,
            km.MonsterDatabase.Element.SUPERCOLD,
        ]:
            return "circle.gif"
        if self.element == km.MonsterDatabase.Element.COLD:
            return "snowflake.gif"
        if self.element == km.MonsterDatabase.Element.HOT:
            return "fire.gif"
        if self.element == km.MonsterDatabase.Element.SLEAZE:
            return "wink.gif"
        if self.element == km.MonsterDatabase.Element.SPOOKY:
            return "skull.gif"
        if self.element == km.MonsterDatabase.Element.STENCH:
            return "stench.gif"
        return ""


@on_kolmafia_start
def initialize_element_instances():
    Element.NONE = Element()
    Element.COLD = Element("cold")
    Element.HOT = Element("hot")
    Element.SLEAZE = Element("sleaze")
    Element.SPOOKY = Element("spooky")
    Element.STENCH = Element("stench")
    Element.SLIME = Element("slime")
    Element.SUPERCOLD = Element("supercold")
    Element.BADSPELLING = Element("bad spelling")
    Element.SHADOW = Element("shadow")
