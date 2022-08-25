from pymafia import ash, utils
from pymafia.datatypes import Item

ITEM = Item("Kramco Sausage-o-Matic™")


def have() -> bool:
    """Return True if the player has the Kramco Sausage-o-Matic™ available, False otherwise."""
    return utils.have(ITEM)


def is_fight_ready() -> bool:
    """Return True if the maximum turns between sausage goblins has been reached, False otherwise."""
    if not have():
        return False

    total_fought = utils.get_property("_sausageFights", int)
    last_turn = utils.get_property("_lastSausageMonsterTurn", int)
    ready_on = last_turn + 4 + 3 * total_fought + max(0, total_fought - 5) ** 3
    return ash.total_turns_played() >= ready_on
