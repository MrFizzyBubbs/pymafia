from enum import Enum

from pymafia import ash, player
from pymafia.combat import Macro
from pymafia.datatypes import Item, Monster
from pymafia.preference import get_property

ITEM = Item("Witchess Set")


class Piece(Enum):
    PAWN = Monster("Witchess Pawn")
    KNIGHT = Monster("Witchess Knight")
    BISHOP = Monster("Witchess Bishop")
    ROOK = Monster("Witchess Rook")
    OX = Monster("Witchess Ox")
    KING = Monster("Witchess King")
    WITCH = Monster("Witchess Witch")
    QUEEN = Monster("Witchess Queen")


def have() -> bool:
    """Return True if the player has the Witchess Set in their campground, False otherwise."""
    return ITEM in ash.get_campground()


def fights_today() -> int:
    """Return the number of Witchess fights used today."""
    return get_property("_witchessFights", int)


def fights_left() -> int:
    """Return the number of Witchess fights left today."""
    return 5 - fights_today()


def fight(piece: Piece, macro: Macro = Macro()) -> bool:
    """Fight a Witchess piece."""
    if not have():
        return False
    if fights_left() < 1:
        return False

    ash.visit_url("campground.php?action=witchess")
    ash.run_choice(1)
    ash.visit_url(
        f"choice.php?option=1&pwd&whichchoice=1182&piece={piece.value.id}",
        False,
    )
    if not player.in_combat(piece.value):
        return False
    ash.run_combat(str(macro))
    return True
