from enum import IntEnum
from typing import Tuple

from pymafia import ash, utils
from pymafia.datatypes import Familiar, Item

FAMILIAR = Familiar("Crimbo Shrub")
DECORATIONS = Item("box of old Crimbo decorations")


class Topper(IntEnum):
    MUSCLE = 1
    MYSTICALITY = 2
    MOXIE = 3


class Lights(IntEnum):
    PRISMATIC = 1
    HOT = 2
    COLD = 3
    STENCH = 4
    SPOOKY = 5
    SLEAZE = 6


class Garland(IntEnum):
    HP = 1
    PVP = 2
    BLOCKING = 3


class Gift(IntEnum):
    YELLOW = 1
    MEAT = 2
    GIFTS = 3


def have() -> bool:
    """Return True is the player has the Crimbo Shrub in their terrarium, False otherwise."""
    return utils.have(FAMILIAR)


def is_decorated() -> bool:
    """Return True if the Crimbo Shrub has been decorated today, False otherwise."""
    return utils.get_property("_shrubDecorated", bool)


def current_decorations() -> Tuple[Topper, Lights, Garland, Gift]:
    """Current Crimbo Shrub decorations."""
    return (
        Topper(utils.get_property("shrubTopper")),
        Lights(utils.get_property("shrubLights")),
        Garland(utils.get_property("shrubGarland")),
        Gift(utils.get_property("shrubGifts")),
    )


def decorate(topper: Topper, lights: Lights, garland: Garland, gift: Gift) -> bool:
    """Decorate the Crimbo Shrub."""
    if not have():
        return False
    if is_decorated():
        return current_decorations() == (topper, lights, garland, gift)

    if not utils.have(DECORATIONS):
        ash.use_familiar(FAMILIAR)
    ash.visit_url(f"inv_use.php?pwd=&which=99&whichitem={DECORATIONS.id}")
    ash.visit_url(
        f"choice.php?whichchoice=999&pwd=&option=1&topper={topper}&lights={lights}&garland={garland}&gift={gift}"
    )
    return True
