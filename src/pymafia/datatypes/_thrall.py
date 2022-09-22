from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from ._skill import Skill


class Thrall:
    id: int = 0
    name: str = "none"
    data: Any = None

    def __init__(self, key: int | str | None = None):
        if key in (None, self.id, self.name):
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
        return hash((self.id, self.name))

    def __eq__(self, other) -> bool:
        return isinstance(other, type(self)) and (self.id, self.name) == (
            other.id,
            other.name,
        )

    def __bool__(self) -> bool:
        return (self.id, self.name) != (type(self).id, type(self).name)

    @classmethod
    def all(cls) -> list[Thrall]:
        from pymafia import ash

        values = km.DataTypes.THRALL_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

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
        from ._skill import Skill

        return Skill(self.data[3] if self else None)

    @property
    def current_modifiers(self) -> str:
        return self.thrall.getCurrentModifiers() if self else ""
