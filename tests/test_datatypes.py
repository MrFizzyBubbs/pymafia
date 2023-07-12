import inspect
from dataclasses import fields

import pytest

from pymafia.datatypes import (
    MAFIA_DATATYPES,
    Bounty,
    Class,
    Coinmaster,
    Effect,
    Element,
    Familiar,
    Item,
    Location,
    Modifier,
    Monster,
    Path,
    Phylum,
    Servant,
    Skill,
    Slot,
    Stat,
    Thrall,
    Vykea,
    VykeaCompanionType,
    VykeaRune,
)

STANDARD_NONE_KEYS = [None, "none", "NONE"]


def get_property_names(cls):
    members = inspect.getmembers(cls, lambda x: isinstance(x, property))
    return [name for (name, _) in members]


@pytest.mark.parametrize(
    "cls,key,expected",
    [
        (Bounty, "bean-shaped rock", ("bean-shaped rock",)),
        *[(Bounty, key, ("none",)) for key in STANDARD_NONE_KEYS],
        *[(Class, key, (1, "Seal Clubber")) for key in [1, "Seal Clubber"]],
        *[(Class, key, (-1, "none")) for key in [*STANDARD_NONE_KEYS, -1]],
        (Coinmaster, "Altar of Bones", ("Altar of Bones",)),
        *[(Coinmaster, key, ("none",)) for key in STANDARD_NONE_KEYS],
        (Effect, 1, (1, "Light!")),
        (Effect, "Light!", (1, "Light!")),
        *[(Effect, key, (1, "Light!")) for key in [1, "Light!"]],
        *[(Effect, key, (-1, "none")) for key in [*STANDARD_NONE_KEYS, -1]],
        (Element, "cold", ("cold",)),
        *[(Element, key, ("none",)) for key in STANDARD_NONE_KEYS],
        *[(Familiar, key, (1, "Mosquito")) for key in [1, "Mosquito"]],
        *[(Familiar, key, (-1, "none")) for key in [*STANDARD_NONE_KEYS, -1]],
        *[(Item, key, (1, "seal-clubbing club")) for key in [1, "seal-clubbing club"]],
        *[(Item, key, (-1, "none")) for key in [*STANDARD_NONE_KEYS, -1]],
        *[
            (Location, key, (15, "The Spooky Forest"))
            for key in [15, "The Spooky Forest"]
        ],
        *[(Location, key, (-1, "none")) for key in [*STANDARD_NONE_KEYS, -1]],
        *[(Monster, key, (1, "spooky vampire")) for key in [1, "spooky vampire"]],
        *[(Monster, key, (0, "none")) for key in [*STANDARD_NONE_KEYS, 0]],
        *[(Path, key, (1, "Boozetafarian")) for key in [1, "Boozetafarian"]],
        *[(Path, key, (-1, "none")) for key in [*STANDARD_NONE_KEYS, -1]],
        (Phylum, "beast", ("beast",)),
        *[(Phylum, key, ("none",)) for key in STANDARD_NONE_KEYS],
        *[(Servant, key, (7, "Assassin")) for key in [7, "Assassin"]],
        *[(Servant, key, (0, "none")) for key in [*STANDARD_NONE_KEYS, 0]],
        *[(Skill, key, (1, "Liver of Steel")) for key in [1, "Liver of Steel"]],
        *[(Skill, key, (-1, "none")) for key in [*STANDARD_NONE_KEYS, -1]],
        (Slot, "hat", ("hat",)),
        *[(Slot, key, ("none",)) for key in STANDARD_NONE_KEYS],
        (Stat, "Muscle", ("Muscle",)),
        *[(Stat, key, ("none",)) for key in STANDARD_NONE_KEYS],
        *[(Thrall, key, (1, "Vampieroghi")) for key in [1, "Vampieroghi"]],
        *[(Thrall, key, (0, "none")) for key in [*STANDARD_NONE_KEYS, 0]],
        (
            Vykea,
            "level 1 blood bookshelf",
            (VykeaCompanionType.BOOKSHELF, VykeaRune.BLOOD, 1),
        ),
        *[
            (Vykea, key, (VykeaCompanionType.NONE, VykeaRune.NONE, 0))
            for key in STANDARD_NONE_KEYS
        ],
        *[(Modifier, key, ("none",)) for key in STANDARD_NONE_KEYS],
        (Modifier, "Absorb Adventures", ("Absorb Adventures",)),
    ],
)
def test_init(cls, key, expected):
    instance = cls(key)
    field_names = [field.name for field in fields(instance) if field.compare]
    field_values = tuple(getattr(instance, name) for name in field_names)
    assert field_values == expected


@pytest.mark.parametrize("cls", MAFIA_DATATYPES)
def test_init_default(cls):
    assert inspect.signature(cls).parameters["key"].default is None


@pytest.mark.parametrize("cls", MAFIA_DATATYPES)
def test_init_invalid(cls):
    with pytest.raises(ValueError):
        cls("")


@pytest.mark.parametrize(
    "cls,expected",
    [
        (Bounty, "bean-shaped rock"),
        (Class, "Seal Clubber"),
        (Coinmaster, "Altar of Bones"),
        (Effect, "Light!"),
        (Effect, "[800]Chocolate Reign"),
        (Element, "cold"),
        (Familiar, "Mosquito"),
        (Item, "seal-clubbing club"),
        (Item, "[10883]astral energy drink"),
        (Location, "The Spooky Forest"),
        (Monster, "spooky vampire"),
        (Monster, "[2050]Jerry Bradford"),
        (Path, "Boozetafarian"),
        (Phylum, "beast"),
        (Servant, "Assassin"),
        (Skill, "Liver of Steel"),
        (Skill, "[7094]Static Shock"),
        (Slot, "hat"),
        (Stat, "Muscle"),
        (Thrall, "Vampieroghi"),
        (Vykea, "level 1 blood bookshelf"),
        (Modifier, "Absorb Adventures"),
    ],
)
def test_str(cls, expected):
    assert str(cls(expected)) == expected


@pytest.mark.parametrize("cls", MAFIA_DATATYPES)
def test_bool(cls):
    assert not bool(cls(None))


@pytest.mark.parametrize("cls", MAFIA_DATATYPES)
def test_all_are_unique(cls):
    all_values = cls.all()
    assert len(set(all_values)) == len(all_values)


@pytest.mark.parametrize("cls", MAFIA_DATATYPES)
def test_all_are_serializable(cls):
    all_values = cls.all()
    assert all_values == [cls(str(x)) for x in all_values]


@pytest.mark.parametrize("cls", MAFIA_DATATYPES)
def test_all_are_true(cls):
    assert all(cls.all())


@pytest.mark.parametrize(
    "cls,key,name",
    [
        *[
            (Bounty, key, name)
            for key in ["bean-shaped rock", None]
            for name in get_property_names(Bounty)
        ],
        *[
            (Class, key, name)
            for key in ["Seal Clubber", None]
            for name in get_property_names(Class)
        ],
        *[
            (Coinmaster, key, name)
            for key in ["Altar of Bones", None]
            for name in get_property_names(Coinmaster)
        ],
        *[
            (Effect, key, name)
            for key in ["Light!", None]
            for name in get_property_names(Effect)
        ],
        *[
            (Element, key, name)
            for key in ["cold", None]
            for name in get_property_names(Element)
        ],
        *[
            (Familiar, key, name)
            for key in ["Mosquito", None]
            for name in get_property_names(Familiar)
        ],
        *[
            (Item, key, name)
            for key in ["seal-clubbing club", None]
            for name in get_property_names(Item)
        ],
        *[
            (Location, key, name)
            for key in ["The Spooky Forest", None]
            for name in get_property_names(Location)
        ],
        *[
            (Monster, key, name)
            for key in ["spooky vampire", None]
            for name in get_property_names(Monster)
        ],
        *[
            (Path, key, name)
            for key in ["Boozetafarian", None]
            for name in get_property_names(Path)
        ],
        *[
            (Phylum, key, name)
            for key in ["beast", None]
            for name in get_property_names(Phylum)
        ],
        *[
            (Servant, key, name)
            for key in ["Assassin", None]
            for name in get_property_names(Servant)
        ],
        *[
            (Skill, key, name)
            for key in ["Liver of Steel", None]
            for name in get_property_names(Skill)
        ],
        *[
            (Slot, key, name)
            for key in ["hat", None]
            for name in get_property_names(Slot)
        ],
        *[
            (Stat, key, name)
            for key in ["Muscle", None]
            for name in get_property_names(Stat)
        ],
        *[
            (Thrall, key, name)
            for key in ["Vampieroghi", None]
            for name in get_property_names(Thrall)
        ],
        *[
            (Vykea, key, name)
            for key in ["level 1 blood bookshelf", None]
            for name in get_property_names(Vykea)
        ],
        *[
            (Modifier, key, name)
            for key in ["Absorb Adventures", None]
            for name in get_property_names(Modifier)
        ],
    ],
)
def test_property(cls, key, name):
    getattr(cls(key), name)
