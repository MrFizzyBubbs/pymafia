from pymafia import ash
from pymafia.datatypes import Location
from pymafia.utils import get_property

location = Location("The X-32-F Combat Training Snowman")

setting_choices = {
    "MUSCLE": 1,
    "MYSTICALITY": 2,
    "MOXIE": 3,
    "TOURNAMENT": 4,
}


def have():
    """Return True if the player has The Snojo available, False otherwise"""
    return get_property("snojoAvailable", bool)


def setting():
    """Return the current snojo setting."""
    return get_property("snojoSetting")


def free_fights_today():
    """Return the number of free snojo fights used today."""
    return get_property("_snojoFreeFights", int)


def free_fights_left():
    """Return the number of free snojo fights left today."""
    return 10 - free_fights_today()


def change_setting(new_setting):
    """Change the snojo setting."""
    if not have():
        raise RuntimeError("need access to The Snojo")
    if new_setting == setting():
        return

    choice = setting_choices[new_setting]
    ash.visit_url("place.php?whichplace=snojo&action=snojo_controller")
    ash.run_choice(choice)

    if setting() != new_setting:
        raise RuntimeError("failed to change snojo setting")
