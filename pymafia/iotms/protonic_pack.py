from enum import Enum
from pymafia import ash, utils
from pymafia.datatypes import Item, Location, Monster

ITEM = Item("protonic accelerator pack")

class Ghost(Enum):
    OILY = Monster("the ghost of Oily McBindle")
    SKIN = Monster("boneless blobghost")
    BAGEL = Monster("the ghost of Monsieur Baguelle")
    HORSE = Monster("The Headless Horseman")
    ICEWOMAN = Monster("The Icewoman")
    SCREEGE =  Monster("The ghost of Ebenoozer Screege")
    SRAVEN = Monster("The ghost of Lord Montague Spookyraven")
    HIPPY = Monster('the ghost of Vanillica "Trashblossom" Gorton')
    FLAME = Monster("the ghost of Sam McGee")
    CENSOR = Monster("The ghost of Richard Cockingham")
    WALDO = Monster("The ghost of Waldo the Carpathian")
    LIME = Monster("Emily Koops, a spooky lime")
    FORTUNADO = Monster("The ghost of Jim Unfortunato")


def have() -> bool:
    """Return True if the player has the protonic accelerator pack available, False otherwise."""
    return utils.have(ITEM)


def ghost_location() -> Location:
    """Return the current location of the protonic ghost."""
    return utils.get_property("ghostLocation", Location)


def streams_crossed() -> bool:
    """Return True if the player has crossed streams today, False otherwise."""
    return utils.get_property("_streamsCrossed", bool)


def cross_streams() -> bool:
    """Cross streams with the target in preference "streamCrossDefaultTarget"."""
    if not have():
        return False
    if streams_crossed():
        return True

    return ash.cli_execute("crossstreams")
