import re

from pymafia import ash
from pymafia.datatypes import Effect, Familiar, Item, Monster, Servant, Skill


def have(thing: Effect | Familiar | Item | Servant | Skill, quantity: int = 1) -> bool:
    """Return whether the player "has" any entity which one could feasibly "have"."""
    if isinstance(thing, Effect):
        return ash.have_effect(thing) >= quantity
    if isinstance(thing, Familiar):
        return ash.have_familiar(thing)
    if isinstance(thing, Item):
        return ash.available_amount(thing) >= quantity
    if isinstance(thing, Servant):
        return ash.have_servant(thing)
    if isinstance(thing, Skill):
        return ash.have_skill(thing)
    raise TypeError(f"unexpected type {type(thing).__name__!r}")


def in_choice(choice: int | str) -> bool:
    """Return whether the player is handling a particular choice adventure."""
    return ash.handling_choice() and ash.last_choice() == int(choice)


def in_combat(monster: Monster | None = None) -> bool:
    """Return where the player is in combat with a particular monster."""
    if ash.current_round() < 1:
        return False
    if monster is None:
        return True

    page = ash.visit_url("fight.php")
    match = re.search("<!-- MONSTERID: (\\d+) -->", page)
    if not match:
        raise RuntimeError("unable to identify monster")
    return int(match.group(1)) == monster.id


def can_visit_url() -> bool:
    """Return whether the player can visit an in-game url."""
    return not (
        ash.current_round() > 0
        or ash.in_multi_fight()
        or ash.fight_follows_choice()
        or ash.handling_choice()
    )
