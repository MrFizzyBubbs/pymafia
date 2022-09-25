from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from .skill import Skill


@total_ordering
class Thrall:
    id: int = 0
    name: str = "none"
    data: Any = None

    def __init__(self, key: int | str | None = None):
        if key in (None, self.name, self.id):
            return

        data = (
            km.PastaThrallData.typeToData(key)
            if isinstance(key, str)
            else km.PastaThrallData.idToData(key)
        )
        if data is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = data[1]
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
    def all(cls) -> list[Thrall]:
        from pymafia import ash

        values = km.DataTypes.THRALL_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def thrall(self) -> Any:
        return km.KoLCharacter.findPastaThrall(self.name)

    @property
    def level(self) -> int:
        return self.thrall.getLevel() if self else 0

    @property
    def image(self) -> str:
        return self.data[6] if self else ""

    @property
    def tinyimage(self) -> str:
        return self.data[7] if self else ""

    @property
    def skill(self) -> Skill:
        from .skill import Skill

        return Skill(self.data[3] if self else None)

    @property
    def current_modifiers(self) -> str:
        return self.thrall.getCurrentModifiers() if self else ""
