import inspect

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
)

STANDARD_NONE_KEYS = [None, "none", "NONE"]


def fields(obj):
    if isinstance(obj, (Bounty, Coinmaster, Element, Phylum, Slot, Stat)):
        return obj.name
    if isinstance(obj, (Class, Effect, Familiar, Location, Monster, Path, Servant, Skill, Item)):  # fmt: skip
        return (obj.id, obj.name)
    if isinstance(obj, Thrall):
        return (obj.id, obj.type_)
    if isinstance(obj, Vykea):
        return (obj.type_, obj.rune, obj.level)


def get_property_names(cls):
    members = inspect.getmembers(cls, lambda x: isinstance(x, property))
    return [name for (name, _) in members]


@pytest.mark.parametrize(
    "cls,key,expected",
    [
        (Bounty, "absence of moss", "absence of moss"),
        *[(Bounty, key, "none") for key in STANDARD_NONE_KEYS],
        *[(Class, key, (1, "Seal Clubber")) for key in [1, "Seal Clubber"]],
        *[(Class, key, (-1, "none")) for key in [*STANDARD_NONE_KEYS, -1]],
        (Coinmaster, "Hermit", "Hermit"),
        *[(Coinmaster, key, "none") for key in STANDARD_NONE_KEYS],
        (Effect, 1, (1, "Light!")),
        (Effect, "Light!", (1, "Light!")),
        *[(Effect, key, (1, "Light!")) for key in [1, "Light!"]],
        *[(Effect, key, (-1, "none")) for key in [*STANDARD_NONE_KEYS, -1]],
        (Element, "cold", "cold"),
        *[(Element, key, "none") for key in STANDARD_NONE_KEYS],
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
        *[(Path, key, (0, "none")) for key in [*STANDARD_NONE_KEYS, 0]],
        (Phylum, "beast", "beast"),
        *[(Phylum, key, "none") for key in STANDARD_NONE_KEYS],
        *[(Servant, key, (1, "Cat")) for key in [1, "Cat"]],
        *[(Servant, key, (0, "none")) for key in [*STANDARD_NONE_KEYS, 0]],
        *[(Skill, key, (1, "Liver of Steel")) for key in [1, "Liver of Steel"]],
        *[(Skill, key, (-1, "none")) for key in [*STANDARD_NONE_KEYS, -1]],
        (Slot, "acc1", "acc1"),
        *[(Slot, key, "none") for key in STANDARD_NONE_KEYS],
        (Stat, "Moxie", "Moxie"),
        *[(Stat, key, "none") for key in STANDARD_NONE_KEYS],
        *[(Thrall, key, (1, "Vampieroghi")) for key in [1, "Vampieroghi"]],
        *[(Thrall, key, (0, "none")) for key in [*STANDARD_NONE_KEYS, 0]],
        (Vykea, "level 1 bookshelf", (VykeaCompanionType.BOOKSHELF, Item(), 1)),
        *[
            (Vykea, key, (VykeaCompanionType.NONE, Item(), 0))
            for key in STANDARD_NONE_KEYS
        ],
    ],
)
def test_init(cls, key, expected):
    assert fields(cls(key)) == expected


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
        (Bounty, "absence of moss"),
        (Class, "Seal Clubber"),
        (Coinmaster, "Hermit"),
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
        (Servant, "Cat"),
        (Skill, "Liver of Steel"),
        (Skill, "[7094]Static Shock"),
        (Slot, "acc1"),
        (Stat, "Moxie"),
        (Thrall, "Vampieroghi"),
        (Vykea, "level 1 bookshelf"),
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
    "cls,name",
    [(cls, name) for cls in MAFIA_DATATYPES for name in get_property_names(cls)],
)
def test_property(cls, name):
    getattr(cls(), name)
