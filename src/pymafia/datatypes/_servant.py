from __future__ import annotations

from functools import total_ordering
from typing import Any

from pymafia.kolmafia import km


@total_ordering
class Servant:
    id: int = 0
    name: str = "none"
    data: Any = None

    def __init__(self, key: int | str | None = None):
        if key in (None, self.name, self.id):
            return

        data = (
            km.EdServantData.typeToData(key)
            if isinstance(key, str)
            else km.EdServantData.idToData(key)
        )
        if data is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = data[2]
        self.name = data[0]
        self.data = data

    def __str__(self) -> str:
        return self.name

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
    def all(cls) -> list[Servant]:
        from pymafia import ash

        values = km.DataTypes.SERVANT_TYPE.allValues()
        return sorted(ash.to_python(values))

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
        return self.data[3] if self else ""

    @property
    def level1_ability(self) -> str:
        return self.data[4] if self else ""

    @property
    def level7_ability(self) -> str:
        return self.data[5] if self else ""

    @property
    def level14_ability(self) -> str:
        return self.data[6] if self else ""

    @property
    def level21_ability(self) -> str:
        return self.data[7] if self else ""
