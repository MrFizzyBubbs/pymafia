from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from pymafia.kolmafia import km


@dataclass(frozen=True, order=True)
class Servant:
    NONE: ClassVar[Servant]

    data: Any = field(default=km.DataTypes.SERVANT_INIT.content, compare=False)
    id: int = km.DataTypes.SERVANT_INIT.contentLong
    name: str = km.DataTypes.SERVANT_INIT.contentString

    def __init__(self, key: int | str | None = None):
        if (isinstance(key, str) and key.casefold() == self.name.casefold()) or key in (
            self.id,
            None,
        ):
            return

        data = (
            km.EdServantData.typeToData(key)
            if isinstance(key, str)
            else km.EdServantData.idToData(key)
        )
        if data is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "data", data)
        object.__setattr__(self, "id", km.EdServantData.dataToId(data))
        object.__setattr__(self, "name", km.EdServantData.dataToType(data))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Servant]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.SERVANT_TYPE.allValues()
        return from_java(values)

    @property
    def servant(self) -> Any:
        return km.EdServantData.findEdServant(self.name)

    @property
    def level(self) -> int:
        return self.servant.getLevel() if self.servant is not None else 0

    @property
    def experience(self) -> int:
        return self.servant.getExperience() if self.servant is not None else 0

    @property
    def image(self) -> str:
        return km.EdServantData.dataToImage(self.data) if self.data is not None else ""

    @property
    def level1_ability(self) -> str:
        return (
            km.EdServantData.dataToLevel1Ability(self.data)
            if self.data is not None
            else ""
        )

    @property
    def level7_ability(self) -> str:
        return (
            km.EdServantData.dataToLevel7Ability(self.data)
            if self.data is not None
            else ""
        )

    @property
    def level14_ability(self) -> str:
        return (
            km.EdServantData.dataToLevel14Ability(self.data)
            if self.data is not None
            else ""
        )

    @property
    def level21_ability(self) -> str:
        return (
            km.EdServantData.dataToLevel21Ability(self.data)
            if self.data is not None
            else ""
        )


Servant.NONE = Servant()
