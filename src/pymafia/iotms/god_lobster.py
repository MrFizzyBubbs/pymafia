from enum import Enum, IntEnum

from pymafia import ash, player
from pymafia.combat import Macro
from pymafia.datatypes import Familiar, Item
from pymafia.preference import get_property

FAMILIAR = Familiar("God Lobster")


class Reward(IntEnum):
    REGALIA = 1
    BLESSING = 2
    EXPERIENCE = 3


class Regalia(Enum):
    SCEPTER = Item("God Lobster's Scepter")
    RING = Item("God Lobster's Ring")
    ROD = Item("God Lobster's Rod")
    ROBE = Item("God Lobster's Robe")
    CROWN = Item("God Lobster's Crown")


def have() -> bool:
    """Return True if the player has the God Lobster in their terrarium, False otherwise."""
    return player.have(FAMILIAR)


def fights_today() -> int:
    """Return the number of God Lobster fights used today."""
    return get_property("godLobsterFights", int)


def fights_left() -> int:
    """Return the number of God Lobster fights remaining today."""
    return 3 - fights_today()


def fight(reward: Reward, macro: Macro = Macro()) -> bool:
    """Fight the God Lobster and choose a reward."""
    if not have():
        return False
    if fights_left() < 1:
        return False

    ash.use_familiar(FAMILIAR)
    ash.visit_url("main.php?fightgodlobster=1")
    ash.run_combat(str(macro))
    ash.run_choice(int(reward))
    return True
