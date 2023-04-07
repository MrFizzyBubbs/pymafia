import pytest

from pymafia.datatypes import Monster
from tests import common


def test_init_from_int():
    monster = Monster(1)
    assert (monster.id, monster.name) == (1, "spooky vampire")


def test_init_from_string():
    monster = Monster("spooky vampire")
    assert (monster.id, monster.name) == (1, "spooky vampire")


def test_init_from_string_incorrect_case():
    monster = Monster("sPoOkY vAmPiRe")
    assert (monster.id, monster.name) == (1, "spooky vampire")


def test_init_from_none():
    monster = Monster(None)
    assert (monster.id, monster.name) == (0, "none")


def test_init_from_default():
    monster = Monster()
    assert (monster.id, monster.name) == (0, "none")


def test_init_invalid():
    with pytest.raises(ValueError):
        Monster("")


def test_str_for_unique_name():
    assert str(Monster("spooky vampire")) == "spooky vampire"


def test_str_for_non_unique_name():
    assert str(Monster("[2050]Jerry Bradford")) == "[2050]Jerry Bradford"


def test_repr():
    assert repr(Monster("spooky vampire")) == "Monster('spooky vampire')"


def test_hash():
    assert hash(Monster("spooky vampire")) == hash((1, "spooky vampire"))


def test_eq():
    assert Monster(1) == Monster(1)


def test_lt():
    assert Monster(1) < Monster(3)


def test_bool_is_true():
    assert bool(Monster(1))


def test_bool_is_false():
    assert not bool(Monster(None))


def test_all_are_unique():
    monsters = Monster.all()
    assert len(set(monsters)) == len(monsters)


def test_all_are_serializable():
    monsters = Monster.all()
    assert monsters == [Monster(str(monster)) for monster in monsters]


def test_all_are_true():
    assert all(Monster.all())


@pytest.mark.parametrize(
    "name",
    common.get_property_names(Monster),
)
def test_property(name):
    getattr(Monster(1), name)
