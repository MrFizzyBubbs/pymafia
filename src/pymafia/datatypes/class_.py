from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, ClassVar

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.stat import Stat


@dataclass(frozen=True, order=True)
class Class:
    NONE: ClassVar[Class]
    SEAL_CLUBBER: ClassVar[Class]
    TURTLE_TAMER: ClassVar[Class]
    PASTAMANCER: ClassVar[Class]
    SAUCEROR: ClassVar[Class]
    DISCO_BANDIT: ClassVar[Class]
    ACCORDION_THIEF: ClassVar[Class]
    AVATAR_OF_BORIS: ClassVar[Class]
    ZOMBIE_MASTER: ClassVar[Class]
    AVATAR_OF_JARLSBERG: ClassVar[Class]
    AVATAR_OF_SNEAKY_PETE: ClassVar[Class]
    ED_THE_UNDYING: ClassVar[Class]
    COW_PUNCHER: ClassVar[Class]
    BEANSLINGER: ClassVar[Class]
    SNAKE_OILER: ClassVar[Class]
    GELATINOUS_NOOB: ClassVar[Class]
    VAMPYRE: ClassVar[Class]
    PLUMBER: ClassVar[Class]
    GREY_GOO: ClassVar[Class]
    PIG_SKINNER: ClassVar[Class]
    CHEESE_WIZARD: ClassVar[Class]
    JAZZ_AGENT: ClassVar[Class]

    ascension_class: Any = field(default=km.DataTypes.CLASS_INIT.content, compare=False)
    id: int = km.DataTypes.CLASS_INIT.contentLong
    name: str = km.DataTypes.CLASS_INIT.contentString

    def __init__(self, key: int | str | None = None):
        if (isinstance(key, str) and key.casefold() == self.name.casefold()) or key in (
            self.id,
            None,
        ):
            return

        ascension_class = km.AscensionClass.find(key)
        if ascension_class is None or ascension_class.getId() < 0:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "ascension_class", ascension_class)
        object.__setattr__(self, "id", ascension_class.getId())
        object.__setattr__(self, "name", ascension_class.getName())

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Class]:
        from pymafia.ash import from_java

        values = km.DataTypes.CLASS_TYPE.allValues()
        return sorted(from_java(values))

    @property
    def primestat(self) -> Stat:
        from pymafia.datatypes.stat import Stat

        if self.ascension_class is None:
            return Stat()
        prime_index = self.ascension_class.getPrimeStatIndex()
        name = km.AdventureResult.STAT_NAMES[prime_index]
        return Stat(name)


Class.NONE = Class()
Class.SEAL_CLUBBER = Class("Seal Clubber")
Class.TURTLE_TAMER = Class("Turtle Tamer")
Class.PASTAMANCER = Class("Pastamancer")
Class.SAUCEROR = Class("Sauceror")
Class.DISCO_BANDIT = Class("Disco Bandit")
Class.ACCORDION_THIEF = Class("Accordion Thief")
Class.AVATAR_OF_BORIS = Class("Avatar of Boris")
Class.ZOMBIE_MASTER = Class("Zombie Master")
Class.AVATAR_OF_JARLSBERG = Class("Avatar of Jarlsberg")
Class.AVATAR_OF_SNEAKY_PETE = Class("Avatar of Sneaky Pete")
Class.ED_THE_UNDYING = Class("Ed the Undying")
Class.COW_PUNCHER = Class("Cow Puncher")
Class.BEANSLINGER = Class("Beanslinger")
Class.SNAKE_OILER = Class("Snake Oiler")
Class.GELATINOUS_NOOB = Class("Gelatinous Noob")
Class.VAMPYRE = Class("Vampyre")
Class.PLUMBER = Class("Plumber")
Class.GREY_GOO = Class("Grey Goo")
Class.PIG_SKINNER = Class("Pig Skinner")
Class.CHEESE_WIZARD = Class("Cheese Wizard")
Class.JAZZ_AGENT = Class("Jazz Agent")
