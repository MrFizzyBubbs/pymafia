from __future__ import annotations

from functools import total_ordering
from typing import Any

from pymafia.kolmafia import km


@total_ordering
class Path:
    id: int = 0
    name: str = "none"
    ascension_path: Any = None

    def __init__(self, key: int | str | None = None):
        if key in (None, self.name, self.id):
            return

        ascension_path = (
            km.AscensionPath.nameToPath(key)
            if isinstance(key, str)
            else km.AscensionPath.idToPath(key)
        )
        if ascension_path == getattr(km, "AscensionPath$Path").NONE:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = ascension_path.getId()
        self.name = ascension_path.getName()
        self.ascension_path = ascension_path

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
    def all(cls) -> list[Path]:
        from pymafia import ash

        values = km.DataTypes.PATH_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def avatar(self) -> bool:
        return self.ascension_path.isAvatar()

    @property
    def image(self) -> str:
        return self.ascension_path.getImage()

    @property
    def points(self) -> int:
        return self.ascension_path.getPoints()

    @property
    def familiars(self) -> bool:
        return self.ascension_path.canUseFamiliars()
