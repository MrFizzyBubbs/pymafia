from pymafia import ash, player
from pymafia.datatypes import Familiar
from pymafia.preference import get_property

FAMILIAR = Familiar("Pair of Stomping Boots")


def have() -> bool:
    """Return True if the player has the Pair of Stomping Boots in their terrarium, False otherwise."""
    return player.have(FAMILIAR)


def runaways_used() -> int:
    """Return the number of free bander runaways used today."""
    return get_property("banderRunaways", int)


def runaways_left() -> int:
    """Return the total number of free bander runaways the player can get from their Stomping Boots."""
    return (ash.familiar_weight(FAMILIAR) + ash.weight_adjustment()) // 5
