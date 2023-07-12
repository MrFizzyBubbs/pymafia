__all__ = [
    "Bounty",
    "BountyType",
    "KoLInternalBountyType",
    "Class",
    "Coinmaster",
    "Effect",
    "EffectQuality",
    "Element",
    "Familiar",
    "Item",
    "CandyType",
    "Location",
    "Modifier",
    "Monster",
    "Path",
    "Phylum",
    "Servant",
    "Skill",
    "Slot",
    "Stat",
    "Thrall",
    "Vykea",
    "VykeaCompanionType",
    "VykeaRune",
]

from pymafia.datatypes.bounty import Bounty, BountyType, KoLInternalBountyType
from pymafia.datatypes.class_ import Class
from pymafia.datatypes.coinmaster import Coinmaster
from pymafia.datatypes.effect import Effect, EffectQuality
from pymafia.datatypes.element import Element
from pymafia.datatypes.familiar import Familiar
from pymafia.datatypes.item import CandyType, Item
from pymafia.datatypes.location import Location
from pymafia.datatypes.modifier import Modifier
from pymafia.datatypes.monster import Monster
from pymafia.datatypes.path import Path
from pymafia.datatypes.phylum import Phylum
from pymafia.datatypes.servant import Servant
from pymafia.datatypes.skill import Skill
from pymafia.datatypes.slot import Slot
from pymafia.datatypes.stat import Stat
from pymafia.datatypes.thrall import Thrall
from pymafia.datatypes.vykea import Vykea, VykeaCompanionType, VykeaRune

MAFIA_DATATYPES = (
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
    Modifier,
)
