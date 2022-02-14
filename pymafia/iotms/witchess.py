from pymafia import ash
from pymafia.combat import Macro
from pymafia.datatypes import Item, Monster
from pymafia.utils import get_property, in_choice, in_combat

item = Item("Witchess Set")

pieces = [
    Monster("Witchess Pawn"),
    Monster("Witchess Knight"),
    Monster("Witchess Bishop"),
    Monster("Witchess Rook"),
    Monster("Witchess Ox"),
    Monster("Witchess King"),
    Monster("Witchess Witch"),
    Monster("Witchess Queen"),
]


def have():
    """Return True if the player has the Witchess Set in their campground, False otherwise."""
    return item in ash.get_campground()


def fights_today():
    """Return the number of Witchess fights used today."""
    return get_property("_witchessFights", int)


def fights_left():
    """Return the number of Witchess fights left today."""
    return 5 - fights_today()


def fight(piece, macro=Macro()):
    """Fight a Witchess piece."""
    if not have():
        raise RuntimeError("need a Witchess Set installed")
    if fights_left() < 1:
        raise RuntimeError("out of Witchess fights")
    if piece not in pieces:
        raise ValueError(f"unknown piece: {piece!r}")

    ash.visit_url("campground.php?action=witchess")
    if not in_choice(1181):
        raise RuntimeError("failed to open Witchess")
    ash.run_choice(1)
    if not in_choice(1182):
        raise RuntimeError("failed to visit shrink ray")
    ash.visit_url(
        f"choice.php?option=1&pwd={ash.my_hash()}&whichchoice=1182&piece={piece.id}",
        False,
    )
    if not in_combat(piece):
        raise RuntimeError("failed to start fight")
    ash.run_combat(macro)
