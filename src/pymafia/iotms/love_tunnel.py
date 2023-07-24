from enum import IntEnum

from pymafia import ash
from pymafia.combat import Macro
from pymafia.datatypes import Location
from pymafia.preference import get_property, set_property

LOCATION = Location("The Tunnel of L.O.V.E.")


class LOVEquipment(IntEnum):
    EARDIGAN = 1
    EPAULETTES = 2
    EARRING = 3


class LOVEffect(IntEnum):
    LOVEBOTAMY = 1
    OPEN_HEART = 2
    WANDERING_EYE = 3


class LOVItem(IntEnum):
    ENAMORANG = 1
    EMOTIONIZER = 2
    CHOCOLATE = 3
    BOUQUET = 4
    ELEPHANT = 5
    TOAST = 6
    NONE = 7


def have() -> bool:
    """Return True if the player has The Tunnel of L.O.V.E available, False otherwise."""
    return get_property("loveTunnelAvailable", bool)


def is_used() -> bool:
    """Return True if The Tunnel of L.O.V.E has been used today, False otherwise."""
    return get_property("_loveTunnelUsed", bool)


def fight_all(
    equipment: LOVEquipment, effect: LOVEffect, item: LOVItem, macro: Macro = Macro()
) -> bool:
    """Fight all LOV monsters and get buffs/equipment."""
    if not have():
        return False
    if is_used():
        return True

    set_property("choiceAdventure1222", 1)  # Entrance
    set_property("choiceAdventure1223", 1)  # Fight LOV Enforcer
    set_property("choiceAdventure1224", int(equipment))
    set_property("choiceAdventure1225", 1)  # Fight LOV Engineer
    set_property("choiceAdventure1226", int(effect))
    set_property("choiceAdventure1227", 1)  # Fight LOV Equivocator
    set_property("choiceAdventure1228", int(item))
    return ash.adv1(LOCATION, -1, str(macro))
