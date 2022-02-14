from pymafia import ash
from pymafia.datatypes import Familiar
from pymafia.utils import get_property
from pymafia.utils import have as _have

familiar = Familiar("Pair of Stomping Boots")


def have():
    """Return True if the player has the Pair of Stomping Boots in their terrarium, False otherwise."""
    return _have(familiar)


def runaways_used():
    """Return the number of free bander runaways used today."""
    return get_property("banderRunaways", int)


def runaways_left():
    """Return the total number of free bander runaways the player can get from their Stomping Boots."""
    return (ash.familiar_weight(familiar) + ash.weight_adjustment()) // 5
