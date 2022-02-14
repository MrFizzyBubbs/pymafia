from pymafia import ash
from pymafia.combat import Macro
from pymafia.datatypes import Familiar, Item
from pymafia.utils import get_property
from pymafia.utils import have as _have

familiar = Familiar("God Lobster")

reward_choices = {"regalia": 1, "blessing": 2, "experience": 3}
regalia = [
    Item("God Lobster's Scepter"),
    Item("God Lobster's Ring"),
    Item("God Lobster's Rod"),
    Item("God Lobster's Robe"),
    Item("God Lobster's Crown"),
]


def have():
    """Return True if the player has the God Lobster in their terrarium, False otherwise."""
    return _have(familiar)


def fights_today():
    """Return the number of God Lobster fights used today."""
    return get_property("godLobsterFights", int)


def fights_left():
    """Return the number of God Lobster fights remaining today."""
    return 3 - fights_today()


def fight(reward, macro=Macro()):
    """Fight the God Lobster and choose a reward."""
    if not have():
        raise RuntimeError("need a God Lobster")
    if fights_left() < 1:
        raise RuntimeError("out of God Lobster fights")

    choice = reward_choices[reward]
    ash.use_familiar(familiar)
    initial_fights = fights_today()
    ash.visit_url("main.php?fightgodlobster=1")
    ash.run_combat(macro)
    ash.run_choice(choice)

    if fights_today() != initial_fights + 1:
        raise RuntimeError("failed to fight the God Lobster")
