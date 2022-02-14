from pymafia import ash
from pymafia.utils import get_property


def have():
    """Return True if the player has the Boxing Daycare open, False otherwise."""
    return get_property("daycareOpen", bool)


def daydream():
    """Have a Boxing Daydream."""
    if not have():
        raise RuntimeError("need access to the Boxing Daycare")
    if get_property("_daycareNap", bool):
        return

    ash.cli_execute("daycare item")


def free_scavenge():
    """Free scavenge for gym equipment."""
    if not have():
        raise RuntimeError("need access to the Boxing Daycare")
    if get_property("_daycareGymScavenges", int) > 0:
        return

    ash.visit_url("place.php?whichplace=town_wrong&action=townwrong_boxingdaycare")
    ash.run_choice(3)  # Enter the Boxing Daycare
    ash.run_choice(2)  # Scavenge for gym equipment
    ash.run_choice(5)  # Return to the Lobby
    ash.run_choice(4)  # Leave

    if get_property("_daycareGymScavenges", int) != 1:
        raise RuntimeError("failed to use the free scavenge")
