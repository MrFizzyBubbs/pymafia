import pytest

from pymafia.datatypes import Coinmaster
from tests import common


def test_init_from_string():
    assert Coinmaster("Hermit").name == "Hermit"


def test_init_from_string_incorrect_case():
    assert Coinmaster("hErMiT").name == "Hermit"


def test_init_from_none():
    assert Coinmaster(None).name == "none"


def test_init_from_default():
    assert Coinmaster().name == "none"


def test_init_invalid():
    with pytest.raises(ValueError):
        Coinmaster("")


def test_str():
    assert str(Coinmaster("Hermit")) == "Hermit"


def test_repr():
    assert repr(Coinmaster("Hermit")) == "Coinmaster('Hermit')"


def test_hash():
    assert hash(Coinmaster("Hermit")) == hash("Hermit")


def test_eq():
    assert Coinmaster("Hermit") == Coinmaster("Hermit")


def test_lt():
    assert Coinmaster("Hermit") < Coinmaster("Internet Meme Shop")


def test_bool_is_true():
    assert bool(Coinmaster("Hermit"))


def test_bool_is_false():
    assert not bool(Coinmaster(None))


def test_all_are_unique():
    coinmasters = Coinmaster.all()
    assert len(set(coinmasters)) == len(coinmasters)


def test_all_are_serializable():
    coinmasters = Coinmaster.all()
    assert coinmasters == [Coinmaster(str(coinmaster)) for coinmaster in coinmasters]


def test_all_are_true():
    assert all(Coinmaster.all())


@pytest.mark.parametrize(
    "name",
    common.get_property_names(Coinmaster),
)
def test_property(name):
    getattr(Coinmaster("Hermit"), name)
