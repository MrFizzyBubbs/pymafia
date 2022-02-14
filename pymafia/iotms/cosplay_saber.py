from pymafia import ash
from pymafia.datatypes import Item
from pymafia.utils import get_property
from pymafia.utils import have as _have

item = Item("Fourth of May Cosplay Saber")
upgrade_choices = {"mp": 1, "ml": 2, "resistance": 3, "familiar": 4}


def have():
    """Return True if the player has the Fourth of May Cosplay Saber available, False otherwise."""
    return _have(item)


def current_upgrade():
    """Return the current Fourth of May Cosplay Saber upgrade."""
    mod = get_property("_saberMod", int)
    for name, choice in upgrade_choices.items():
        if choice == mod:
            return name
    return None


def is_upgraded():
    """Return True if the Fourth of May Cosplay Saber has been upgraded today, False otherwise."""
    return current_upgrade() is not None


def upgrade(new_upgrade):
    """Upgrade the Fourth of May Cosplay Saber."""
    if not have():
        raise RuntimeError("need a Fourth of May Cosplay Saber")
    if is_upgraded() and current_upgrade() == new_upgrade:
        return
    if is_upgraded():
        raise RuntimeError("already upgraded the saber today")
    if new_upgrade not in upgrade_choices:
        raise ValueError(f"unknown upgrade: {new_upgrade!r}")

    ash.cli_execute(f"saber {new_upgrade}")
