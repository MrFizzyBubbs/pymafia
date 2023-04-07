import pytest

from pymafia.datatypes import Item
from tests import common


def test_init_from_int():
    item = Item(1)
    assert (item.id, item.name) == (1, "seal-clubbing club")


def test_init_from_string():
    item = Item("seal-clubbing club")
    assert (item.id, item.name) == (1, "seal-clubbing club")


def test_init_from_string_incorrect_case():
    item = Item("sEaL-cLuBbInG cLuB")
    assert (item.id, item.name) == (1, "seal-clubbing club")


def test_init_from_none():
    item = Item(None)
    assert (item.id, item.name) == (-1, "none")


def test_init_from_default():
    item = Item()
    assert (item.id, item.name) == (-1, "none")


def test_init_invalid():
    with pytest.raises(ValueError):
        Item("")


def test_str_for_unique_name():
    assert str(Item("seal-clubbing club")) == "seal-clubbing club"


def test_str_for_non_unique_name():
    assert str(Item("[10883]astral energy drink")) == "[10883]astral energy drink"


def test_repr():
    assert repr(Item("seal-clubbing club")) == "Item('seal-clubbing club')"


def test_hash():
    assert hash(Item("seal-clubbing club")) == hash((1, "seal-clubbing club"))


def test_eq():
    assert Item(1) == Item(1)


def test_lt():
    assert Item(1) < Item(2)


def test_bool_is_true():
    assert bool(Item(1))


def test_bool_is_false():
    assert not bool(Item(None))


def test_all_are_unique():
    items = Item.all()
    assert len(set(items)) == len(items)


def test_all_are_serializable():
    items = Item.all()
    assert items == [Item(str(item)) for item in items]


def test_all_are_true():
    assert all(Item.all())


@pytest.mark.parametrize(
    "name",
    common.get_property_names(Item),
)
def test_property(name):
    getattr(Item(1), name)
