from pymafia import ash, player
from pymafia.combat import Macro
from pymafia.datatypes import Location, Monster, Skill
from pymafia.preference import get_property

PASSIVE = Skill("Comprehensive Cartography")
SKILL = Skill("Map the Monsters")


def have() -> bool:
    """Return True if the player has the Comprehensive Cartography skill, False otherwise."""
    return player.have(PASSIVE)


def monsters_mapped() -> int:
    """Return the number of Map the Monsters skill uses today."""
    return get_property("_monstersMapped", int)


def map_monster(location: Location, monster: Monster, macro: Macro = Macro()) -> bool:
    """Map to a monster in a location."""
    if not have():
        return False
    if monsters_mapped() >= 3:
        return False
    if not ash.can_adventure(location):
        return False

    if not get_property("mappingMonsters", bool):
        ash.use_skill(SKILL)

    turns = ash.my_turncount()
    while not player.in_combat():
        if ash.my_turncount() > turns:
            raise RuntimeError("Map the Monsters unsuccessful?")
        ash.visit_url(location.url)
        if player.in_choice(1435):
            ash.run_choice(1, False, f"heyscriptswhatsupwinkwink={monster.id}")
            ash.run_combat(str(macro))
            return True
        else:
            ash.run_choice(-1, False)
    return False
