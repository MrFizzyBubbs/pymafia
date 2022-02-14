from pymafia import ash
from pymafia.datatypes import Item
from pymafia.utils import get_property
from pymafia.utils import have as _have

item = Item("mumming trunk")

costume_choices = {
    "meat": 0,
    "mp": 1,
    "musc": 2,
    "item": 3,
    "myst": 4,
    "hp": 5,
    "mox": 6,
}


def have():
    """Return True if the player has the mumming trunk available, False otherwise."""
    return _have(item)


def costumes_used():
    """Return a list of the costumes applied today."""
    uses = [int(x) for x in get_property("_mummeryUses").split(",") if x]
    return [name for name, choice in costume_choices.items() if choice in uses]


def apply_costume(costume):
    """Dress up the player's current familiar with a costume."""
    if not have():
        raise RuntimeError("need a mumming trunk")
    if costume in costumes_used():
        raise RuntimeError(f"already applied the {costume!r} costume today")
    if not ash.my_familiar():
        raise RuntimeError("need to have a familiar to put a costume on")

    choice = costume_choices[costume]
    ash.cli_execute(f"mummery {choice}")
