from enum import IntEnum

from pymafia import ash, player
from pymafia.datatypes import Item
from pymafia.preference import get_property

ITEM = Item("Fourth of May Cosplay Saber")


class Upgrade(IntEnum):
    NONE = 0
    MP = 1
    ML = 2
    RESISTANCE = 3
    FAMILIAR = 4


def have() -> bool:
    """Return True if the player has the Fourth of May Cosplay Saber available, False otherwise."""
    return player.have(ITEM)


def current_upgrade() -> Upgrade:
    """Return the current Fourth of May Cosplay Saber upgrade."""
    return Upgrade(get_property("_saberMod", int))


def is_upgraded() -> bool:
    """Return True if the Fourth of May Cosplay Saber has been upgraded today, False otherwise."""
    return current_upgrade() is not Upgrade.NONE


def upgrade(new_upgrade: Upgrade) -> bool:
    """Upgrade the Fourth of May Cosplay Saber."""
    if not have():
        return False
    if is_upgraded():
        return current_upgrade() == new_upgrade

    return ash.cli_execute(f"saber {new_upgrade.name.lower()}")
