from __future__ import annotations

from typing import Any

from pymafia.kolmafia import km


class Path:
    id: int = 0
    name: str = "none"
    ascension_path: Any = None

    def __init__(self, key: int | str | None = None):
        if key in (None, self.id, self.name):
            return

        ascension_path = (
            km.AscensionPath.nameToPath(key)
            if isinstance(key, str)
            else km.AscensionPath.idToPath(key)
        )
        if (
            ascension_path
            == km.autoclass("net/sourceforge/kolmafia/AscensionPath$Path").NONE
        ):
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = ascension_path.getId()
        self.name = ascension_path.getName()
        self.ascension_path = ascension_path

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
    def all(cls) -> list[Path]:
        from pymafia import ash

        values = km.DataTypes.PATH_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

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
