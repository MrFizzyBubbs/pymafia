from .bounty import Bounty
from .class_ import Class
from .coinmaster import Coinmaster
from .effect import Effect
from .element import Element
from .familiar import Familiar
from .item import Item
from .location import Location
from .monster import Monster
from .path import Path
from .phylum import Phylum
from .servant import Servant
from .skill import Skill
from .slot import Slot
from .stat import Stat
from .thrall import Thrall
from .vykea import Vykea

MAFIA_DATATYPES = [
    Item,
    Location,
    Class,
    Stat,
    Skill,
    Effect,
    Familiar,
    Slot,
    Monster,
    Element,
    Coinmaster,
    Phylum,
    Bounty,
    Thrall,
    Servant,
    Vykea,
    Path,
]

__all__ = [
    "Bounty",
    "Class",
    "Coinmaster",
    "Effect",
    "Element",
    "Familiar",
    "Item",
    "Location",
    "Monster",
    "Path",
    "Phylum",
    "Servant",
    "Skill",
    "Slot",
    "Stat",
    "Thrall",
    "Vykea",
]
