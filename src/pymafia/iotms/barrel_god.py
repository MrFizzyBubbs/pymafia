import re

from pymafia import ash
from pymafia.preference import get_property


def have() -> bool:
    """Return True if the player has the shrine to the Barrel god unlocked, False otherwise."""
    return get_property("barrelShrineUnlocked", bool)


def smash_free() -> bool:
    """Smash the free barrels in The Barrel full of Barrels."""
    if not have():
        return False

    pattern = '<div class="ex"><a class="spot" href="([^"]+)"><img title="A barrel"'
    for barrel in re.findall(pattern, ash.visit_url("barrel.php")):
        ash.visit_url(barrel)
    return True
