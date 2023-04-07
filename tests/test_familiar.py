import pytest

from pymafia.datatypes import Familiar
from tests import common


def test_init_from_int():
    familiar = Familiar(1)
    assert (familiar.id, familiar.name) == (1, "Mosquito")


def test_init_from_string():
    familiar = Familiar("Mosquito")
    assert (familiar.id, familiar.name) == (1, "Mosquito")


def test_init_from_string_incorrect_case():
    familiar = Familiar("mOsQuItO")
    assert (familiar.id, familiar.name) == (1, "Mosquito")


def test_init_from_none():
    familiar = Familiar(None)
    assert (familiar.id, familiar.name) == (-1, "none")


def test_init_from_default():
    familiar = Familiar()
    assert (familiar.id, familiar.name) == (-1, "none")


def test_init_invalid():
    with pytest.raises(ValueError):
        Familiar("")


def test_str():
    assert str(Familiar("Mosquito")) == "Mosquito"


def test_repr():
    assert repr(Familiar("Mosquito")) == "Familiar('Mosquito')"


def test_hash():
    assert hash(Familiar("Mosquito")) == hash((1, "Mosquito"))


def test_eq():
    assert Familiar(1) == Familiar(1)


def test_lt():
    assert Familiar(1) < Familiar(2)


def test_bool_is_true():
    assert bool(Familiar(1))


def test_bool_is_false():
    assert not bool(Familiar(None))


def test_all_are_unique():
    familiars = Familiar.all()
    assert len(set(familiars)) == len(familiars)


def test_all_are_serializable():
    familiars = Familiar.all()
    assert familiars == [Familiar(str(familiar)) for familiar in familiars]


def test_all_are_true():
    assert all(Familiar.all())


@pytest.mark.parametrize(
    "name",
    common.get_property_names(Familiar),
)
def test_property(name):
    getattr(Familiar(1), name)
