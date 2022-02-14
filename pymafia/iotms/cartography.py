from pymafia import ash
from pymafia.combat import Macro
from pymafia.datatypes import Skill
from pymafia.utils import get_property
from pymafia.utils import have as _have
from pymafia.utils import in_choice, in_combat

passive = Skill("Comprehensive Cartography")
skill = Skill("Map the Monsters")


def have():
    """Return True if the player has the Comprehensive Cartography skill, False otherwise."""
    return _have(passive)


def monsters_mapped():
    """Return the number of Map the Monsters skill uses today."""
    return get_property("_monstersMapped", int)


def map_monster(location, monster, macro=Macro()):
    """Map to a monster in a location."""
    if not have():
        raise RuntimeError("need the Comprehensive Cartography skill")
    if monsters_mapped() >= 3:
        raise RuntimeError("already mapped three monsters today")

    if not get_property("mappingMonsters"):
        ash.use_skill(skill)
    ash.visit_url(location.url)
    if not in_choice(1435):
        raise RuntimeError("failed to encounter the Leading Yourself Right to Them noncombat adventure")  # fmt: skip
    ash.visit_url(f"choice.php?pwd=&whichchoice=1435&option=1&heyscriptswhatsupwinkwink={monster.id}")  # fmt: skip
    if not in_combat(monster):
        raise RuntimeError(f"failed to start fight with {monster!r}")
    ash.run_combat(macro)
