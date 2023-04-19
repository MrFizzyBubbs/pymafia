from enum import IntEnum
from typing import List

from pymafia import ash, player
from pymafia.datatypes import Familiar, Item
from pymafia.preference import get_property

ITEM = Item("mumming trunk")


class Costume(IntEnum):
    MEAT = 0
    MP = 1
    MUSCLE = 2
    ITEM = 3
    MYST = 4
    HP = 5
    MOXIE = 6


def have() -> bool:
    """Return True if the player has the mumming trunk available, False otherwise."""
    return player.have(ITEM)


def costumes_used() -> List[Costume]:
    """Return a list of the costumes applied today."""
    return [Costume(int(x)) for x in get_property("_mummeryUses").split(",") if x]


def apply_costume(familiar: Familiar, costume: Costume) -> bool:
    """Dress up a familiar with a costume."""
    if not have():
        return False
    if costume in costumes_used():
        return True  # TODO return True if costume is equipped on desired familiar
    if not player.have(familiar):
        return False

    ash.use_familiar(familiar)
    return ash.cli_execute(f"mummery {int(costume)}")
