import pytest

from pymafia.datatypes import Location
from tests import common


def test_init_from_int():
    location = Location(15)
    assert (location.id, location.name) == (15, "The Spooky Forest")


def test_init_from_string():
    location = Location("The Spooky Forest")
    assert (location.id, location.name) == (15, "The Spooky Forest")


def test_init_from_string_incorrect_case():
    location = Location("tHe SpOoKy FoReSt")
    assert (location.id, location.name) == (15, "The Spooky Forest")


def test_init_from_none():
    location = Location(None)
    assert (location.id, location.name) == (-1, "none")


def test_init_from_default():
    location = Location()
    assert (location.id, location.name) == (-1, "none")


def test_init_invalid():
    with pytest.raises(ValueError):
        Location("")


def test_str():
    assert str(Location("The Spooky Forest")) == "The Spooky Forest"


def test_repr():
    assert repr(Location("The Spooky Forest")) == "Location('The Spooky Forest')"


def test_hash():
    assert hash(Location("The Spooky Forest")) == hash((15, "The Spooky Forest"))


def test_eq():
    assert Location(15) == Location(15)


def test_lt():
    assert Location(15) < Location(18)


def test_bool_is_true():
    assert bool(Location(15))


def test_bool_is_false():
    assert not bool(Location(None))


def test_all_are_unique():
    locations = Location.all()
    assert len(set(locations)) == len(locations)


def test_all_are_serializable():
    locations = Location.all()
    assert locations == [Location(str(location)) for location in locations]


def test_all_are_true():
    assert all(Location.all())


@pytest.mark.parametrize(
    "name",
    common.get_property_names(Location),
)
def test_property(name):
    getattr(Location(15), name)
