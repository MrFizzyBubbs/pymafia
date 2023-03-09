from enum import IntEnum

from pymafia import ash, player
from pymafia.datatypes import Element, Item, Stat

ITEM = Item("portable pantogram")
PANTS = Item("pantogram pants")


class PantogramAlignment(IntEnum):
    MUSCLE = 1
    MYSTICALITY = 2
    MOXIE = 3


class PantogramElement(IntEnum):
    HOT = 1
    COLD = 2
    SPOOKY = 3
    SLEAZE = 4
    STENCH = 5


alignments = {Stat("Muscle"): 1, Stat("Mysticality"): 2, Stat("Moxie"): 3}
elements = {
    Element("hot"): 1,
    Element("cold"): 2,
    Element("spooky"): 3,
    Element("sleaze"): 4,
    Element("stench"): 5,
}
left_sacrifices = {
    "Maximum HP: 40": (-1, 0),
    "Maximum MP: 20": (-2, 0),
    "HP Regen Max: 10": (Item("red pixel potion"), 1),
    "HP Regen Max: 15": (Item("royal jelly"), 1),
    "HP Regen Max: 20": (Item("scented massage oil"), 1),
    "MP Regen Max: 10": (Item("Cherry Cloaca Cola"), 1),
    "MP Regen Max: 15": (Item("bubblin' crude"), 1),
    "MP Regen Max: 20": (Item("glowing New Age crystal"), 1),
    "Mana Cost: -3": (Item("baconstone"), 1),
}
right_sacrifices = {
    "Weapon Damage: 20": (-1, 0),
    "Spell Damage Percent: 20": (-2, 0),
    "Meat Drop: 30": (Item("taco shell"), 1),
    "Meat Drop: 60": (Item("porquoise"), 1),
    "Item Drop: 15": (Item("fairy gravy boat"), 1),
    "Item Drop: 30": (Item("tiny dancer"), 1),
    "Muscle Experience: 3": (Item("Knob Goblin firecracker"), 3),
    "Mysticality Experience: 3": (Item("razor-sharp can lid"), 3),
    "Moxie Experience: 3": (Item("spider web"), 3),
    "Muscle Experience Percent: 25": (Item("synthetic marrow"), 5),
    "Mysticality Experience Percent: 25": (Item("haunted battery"), 5),
    "Moxie Experience Percent: 25": (Item("the funk"), 5),
}
middle_sacrifices = {
    "Combat Rate: -5": (-1, 0),
    "Combat Rate: 5": (-2, 0),
    "Critical Hit Percent: 10": (Item("hamethyst"), 1),
    "Initiative: 50": (Item("bar skin"), 1),
    "Familiar Weight: 10": (Item("lead necklace"), 11),
    "Candy Drop: 100": (Item("huge bowl of candy"), 1),
    "Item Drop Penalty: -10": (Item("sea salt crystal"), 11),
    "Fishing Skill: 5": (Item("wriggling worm"), 1),
    "Pool Skill: 5": (Item("8-ball"), 15),
    "Avatar: Purple": (Item("moxie weed"), 99),
    "Drops Items: true": (Item("ten-leaf clover"), 1),
}


def have():
    """Return True if the player has the portable pantogram available, False otherwise."""
    return player.have(ITEM)


def have_pants():
    """Return True if the player has the pantogram pants available today, False otherwise."""
    return player.have(PANTS)


def summon_pants(alignment, element, left, right, middle):
    """Summon pantogram pants."""
    if not have():
        return False
    if have_pants():
        return False  # TODO check enchantments

    m = alignments[alignment]
    e = elements[element]

    sacrifice, quantity = left_sacrifices[left]
    if isinstance(sacrifice, Item) and not player.have(sacrifice, quantity):
        return False
    s1 = f"{int(sacrifice)},{quantity}"

    sacrifice, quantity = right_sacrifices[right]
    if isinstance(sacrifice, Item) and not player.have(sacrifice, quantity):
        return False
    s2 = f"{int(sacrifice)},{quantity}"

    sacrifice, quantity = middle_sacrifices[middle]
    if isinstance(sacrifice, Item) and not player.have(sacrifice, quantity):
        return False
    s3 = f"{int(sacrifice)},{quantity}"

    ash.visit_url(
        f"choice.php?pwd=&whichchoice=1270&option=1&m={m}&e={e}&s1={s1}&s2={s2}&s3={s3}"
    )
    return True
