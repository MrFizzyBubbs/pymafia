from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from pymafia.kolmafia import km


@dataclass(frozen=True, order=True)
class Path:
    NONE: ClassVar[Path]
    BOOZETAFARIAN: ClassVar[Path]
    TEETOTALER: ClassVar[Path]
    OXYGENARIAN: ClassVar[Path]
    BEES_HATE_YOU: ClassVar[Path]
    WAY_OF_THE_SURPRISING_FIST: ClassVar[Path]
    TRENDY: ClassVar[Path]
    AVATAR_OF_BORIS: ClassVar[Path]
    BUGBEAR_INVASION: ClassVar[Path]
    ZOMBIE_SLAYER: ClassVar[Path]
    CLASS_ACT: ClassVar[Path]
    AVATAR_OF_JARLSBERG: ClassVar[Path]
    BIG: ClassVar[Path]
    KOLHS: ClassVar[Path]
    CLASS_ACT_II: ClassVar[Path]
    AVATAR_OF_SNEAKY_PETE: ClassVar[Path]
    SLOW_AND_STEADY: ClassVar[Path]
    HEAVY_RAINS: ClassVar[Path]
    PICKY: ClassVar[Path]
    STANDARD: ClassVar[Path]
    ACTUALLY_ED_THE_UNDYING: ClassVar[Path]
    ONE_CRAZY_RANDOM_SUMMER: ClassVar[Path]
    COMMUNITY_SERVICE: ClassVar[Path]
    AVATAR_OF_WEST_OF_LOATHING: ClassVar[Path]
    THE_SOURCE: ClassVar[Path]
    NUCLEAR_AUTUMN: ClassVar[Path]
    GELATINOUS_NOOB: ClassVar[Path]
    LICENSE_TO_ADVENTURE: ClassVar[Path]
    LIVE_ASCEND_REPEAT: ClassVar[Path]
    POCKET_FAMILIARS: ClassVar[Path]
    G_LOVER: ClassVar[Path]
    DISGUISES_DELIMIT: ClassVar[Path]
    DARK_GYFFTE: ClassVar[Path]
    TWO_CRAZY_RANDOM_SUMMER: ClassVar[Path]
    KINGDOM_OF_EXPLOATHING: ClassVar[Path]
    PATH_OF_THE_PLUMBER: ClassVar[Path]
    LOW_KEY_SUMMER: ClassVar[Path]
    GREY_GOO: ClassVar[Path]
    YOU_ROBOT: ClassVar[Path]
    QUANTUM_TERRARIUM: ClassVar[Path]
    WILDFIRE: ClassVar[Path]
    GREY_YOU: ClassVar[Path]
    JOURNEYMAN: ClassVar[Path]
    FALL_OF_THE_DINOSAURS: ClassVar[Path]
    AVATAR_OF_SHADOWS_OVER_LOATHING: ClassVar[Path]
    BAD_MOON: ClassVar[Path]

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
        from pymafia.ash import from_java

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
Path.BOOZETAFARIAN = Path("Boozetafarian")
Path.TEETOTALER = Path("Teetotaler")
Path.OXYGENARIAN = Path("Oxygenarian")
Path.BEES_HATE_YOU = Path("Bees Hate You")
Path.WAY_OF_THE_SURPRISING_FIST = Path("Way of the Surprising Fist")
Path.TRENDY = Path("Trendy")
Path.AVATAR_OF_BORIS = Path("Avatar of Boris")
Path.BUGBEAR_INVASION = Path("Bugbear Invasion")
Path.ZOMBIE_SLAYER = Path("Zombie Slayer")
Path.CLASS_ACT = Path("Class Act")
Path.AVATAR_OF_JARLSBERG = Path("Avatar of Jarlsberg")
Path.BIG = Path("BIG!")
Path.KOLHS = Path("KOLHS")
Path.CLASS_ACT_II = Path("Class Act II: A Class For Pigs")
Path.AVATAR_OF_SNEAKY_PETE = Path("Avatar of Sneaky Pete")
Path.SLOW_AND_STEADY = Path("Slow and Steady")
Path.HEAVY_RAINS = Path("Heavy Rains")
Path.PICKY = Path("Picky")
Path.STANDARD = Path("Standard")
Path.ACTUALLY_ED_THE_UNDYING = Path("Actually Ed the Undying")
Path.ONE_CRAZY_RANDOM_SUMMER = Path("One Crazy Random Summer")
Path.COMMUNITY_SERVICE = Path("Community Service")
Path.AVATAR_OF_WEST_OF_LOATHING = Path("Avatar of West of Loathing")
Path.THE_SOURCE = Path("The Source")
Path.NUCLEAR_AUTUMN = Path("Nuclear Autumn")
Path.GELATINOUS_NOOB = Path("Gelatinous Noob")
Path.LICENSE_TO_ADVENTURE = Path("License to Adventure")
Path.LIVE_ASCEND_REPEAT = Path("Live. Ascend. Repeat.")
Path.POCKET_FAMILIARS = Path("Pocket Familiars")
Path.G_LOVER = Path("G-Lover")
Path.DISGUISES_DELIMIT = Path("Disguises Delimit")
Path.DARK_GYFFTE = Path("Dark Gyffte")
Path.TWO_CRAZY_RANDOM_SUMMER = Path("Two Crazy Random Summer")
Path.KINGDOM_OF_EXPLOATHING = Path("Kingdom of Exploathing")
Path.PATH_OF_THE_PLUMBER = Path("Path of the Plumber")
Path.LOW_KEY_SUMMER = Path("Low Key Summer")
Path.GREY_GOO = Path("Grey Goo")
Path.YOU_ROBOT = Path("You, Robot")
Path.QUANTUM_TERRARIUM = Path("Quantum Terrarium")
Path.WILDFIRE = Path("Wildfire")
Path.GREY_YOU = Path("Grey You")
Path.JOURNEYMAN = Path("Journeyman")
Path.FALL_OF_THE_DINOSAURS = Path("Fall of the Dinosaurs")
Path.AVATAR_OF_SHADOWS_OVER_LOATHING = Path("Avatar of Shadows Over Loathing")
Path.BAD_MOON = Path("Bad Moon")
