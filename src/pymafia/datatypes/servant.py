from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pymafia.kolmafia import km


@dataclass(frozen=True, order=True)
class Servant:
    id: int = 0
    name: str = "none"

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

        object.__setattr__(self, "id", km.EdServantData.dataToId(data))
        object.__setattr__(self, "name", km.EdServantData.dataToType(data))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return (self.id, self.name) != (type(self).id, type(self).name)

    @classmethod
    def all(cls) -> list[Servant]:
        from pymafia import ash

        values = km.DataTypes.SERVANT_TYPE.allValues()
        return ash.to_python(values)

    @property
    def data(self) -> Any:
        return km.EdServantData.idToData(self.id)

    @property
    def servant(self) -> Any:
        return km.EdServantData.findEdServant(self.name)

    @property
    def level(self) -> int:
        return 0 if self.servant is None else self.servant.getLevel()

    @property
    def experience(self) -> int:
        return 0 if self.servant is None else self.servant.getExperience()

    @property
    def image(self) -> str:
        return km.EdServantData.dataToImage(self.data) if self else ""

    @property
    def level1_ability(self) -> str:
        return km.EdServantData.dataToLevel1Ability(self.data) if self else ""

    @property
    def level7_ability(self) -> str:
        return km.EdServantData.dataToLevel7Ability(self.data) if self else ""

    @property
    def level14_ability(self) -> str:
        return km.EdServantData.dataToLevel14Ability(self.data) if self else ""

    @property
    def level21_ability(self) -> str:
        return km.EdServantData.dataToLevel21Ability(self.data) if self else ""
