from pymafia import ash
from pymafia.preference import get_property


def have() -> bool:
    """Return True if the player has the Boxing Daycare open, False otherwise."""
    return get_property("daycareOpen", bool)


def daydream() -> bool:
    """Have a Boxing Daydream."""
    if not have():
        return False
    if get_property("_daycareNap", bool):
        return True

    return ash.cli_execute("daycare item")


def free_scavenge() -> bool:
    """Free scavenge for gym equipment."""
    if not have():
        return False
    if get_property("_daycareGymScavenges", int) > 0:
        return True

    ash.visit_url("place.php?whichplace=town_wrong&action=townwrong_boxingdaycare")
    ash.run_choice(3)  # Enter the Boxing Daycare
    ash.run_choice(2)  # Scavenge for gym equipment
    ash.run_choice(5)  # Return to the Lobby
    ash.run_choice(4)  # Leave
    return True
