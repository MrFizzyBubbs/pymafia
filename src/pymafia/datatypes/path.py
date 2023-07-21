from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from pymafia.kolmafia import km


@dataclass(frozen=True, order=True)
class Path:
    NONE: ClassVar[Path]

    ascension_path: Any = field(default=km.DataTypes.PATH_INIT.content, compare=False)
    id: int = km.DataTypes.PATH_INIT.contentLong
    name: str = km.DataTypes.PATH_INIT.contentString

    def __init__(self, key: int | str | None = None):
        if (isinstance(key, str) and key.casefold() == self.name.casefold()) or key in (
            self.id,
            None,
        ):
            return

        ascension_path = (
            km.AscensionPath.nameToPath(key)
            if isinstance(key, str)
            else km.AscensionPath.idToPath(key)
        )
        if ascension_path == km.AscensionPath.Path.NONE:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "ascension_path", ascension_path)
        object.__setattr__(self, "id", ascension_path.getId())
        object.__setattr__(self, "name", ascension_path.getName())

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Path]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.PATH_TYPE.allValues()
        return sorted(from_java(values))

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


Path.NONE = Path()
