from enum import IntEnum

from pymafia import ash
from pymafia.datatypes import Location
from pymafia.preference import get_property

LOCATION = Location("The X-32-F Combat Training Snowman")


class Setting(IntEnum):
    MUSCLE = 1
    MYSTICALITY = 2
    MOXIE = 3
    TOURNAMENT = 4


def have() -> bool:
    """Return True if the player has The Snojo available, False otherwise"""
    return get_property("snojoAvailable", bool)


def current_setting() -> Setting:
    """Return the current snojo setting."""
    return Setting[get_property("snojoSetting")]


def free_fights_today() -> int:
    """Return the number of free snojo fights used today."""
    return get_property("_snojoFreeFights", int)


def free_fights_left() -> int:
    """Return the number of free snojo fights left today."""
    return 10 - free_fights_today()


def change_setting(setting: Setting) -> bool:
    """Change the snojo setting."""
    if not have():
        return False
    if current_setting() is setting:
        return True

    ash.visit_url("place.php?whichplace=snojo&action=snojo_controller")
    ash.run_choice(int(setting))
    return True
