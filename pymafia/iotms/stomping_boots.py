from pymafia import ash, utils
from pymafia.datatypes import Familiar

FAMILIAR = Familiar("Pair of Stomping Boots")


def have() -> bool:
    """Return True if the player has the Pair of Stomping Boots in their terrarium, False otherwise."""
    return utils.have(FAMILIAR)


def runaways_used() -> int:
    """Return the number of free bander runaways used today."""
    return utils.get_property("banderRunaways", int)


def runaways_left() -> int:
    """Return the total number of free bander runaways the player can get from their Stomping Boots."""
    return (ash.familiar_weight(FAMILIAR) + ash.weight_adjustment()) // 5
