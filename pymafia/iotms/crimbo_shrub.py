from pymafia import ash
from pymafia.datatypes import Element, Familiar, Item, Stat
from pymafia.utils import get_property
from pymafia.utils import have as _have

familiar = Familiar("Crimbo Shrub")
decorations = Item("box of old Crimbo decorations")

topper_choices = {Stat.MUSCLE: 1, Stat.MYSTICALITY: 2, Stat.MOXIE: 3}
lights_choices = {
    "prismatic": 1,
    Element.HOT: 2,
    Element.COLD: 3,
    Element.STENCH: 4,
    Element.SPOOKY: 5,
    Element.SLEAZE: 6,
}
garland_choices = {"HP": 1, "PvP": 2, "blocking": 3}
gift_choices = {"yellow": 1, "meat": 2, "gifts": 3}


def have():
    """Return True is the player has the Crimbo Shrub in their terrarium, False otherwise."""
    return _have(familiar)


def is_decorated():
    """Return True if the Crimbo Shrub has been decorated today, False otherwise."""
    return get_property("_shrubDecorated", bool)


def check_decorations():
    """Current Crimbo Shrub decorations."""
    return (
        get_property("shrubTopper"),
        get_property("shrubLights"),
        get_property("shrubGarland"),
        get_property("shrubGifts"),
    )


def decorate(topper, lights, garland, gift):
    """Decorate the Crimbo Shrub."""
    if not have():
        raise RuntimeError("need a Crimbo Shrub")
    if is_decorated() and check_decorations() == (topper, lights, garland, gift):
        return
    if is_decorated():
        raise RuntimeError("already been decorated the shrub today")

    choices = (
        topper_choices[topper],
        lights_choices[lights],
        garland_choices[garland],
        gift_choices[gift],
    )
    ash.visit_url(f"inv_use.php?pwd=&which=99&whichitem={decorations.id}")
    ash.visit_url(f"choice.php?whichchoice=999&pwd=&option=1&topper={0}&lights={1}&garland={2}&gift={3}".format(*choices))  # fmt: skip

    if check_decorations() != (topper, lights, garland, gift):
        raise RuntimeError(f"failed to decorate the shrub with {(topper, lights, garland, gift)}")  # fmt: skip
