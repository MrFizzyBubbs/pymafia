import pytest

from pymafia.datatypes import Bounty
from tests import common


def test_init_from_string():
    assert Bounty("absence of moss").name == "absence of moss"


def test_init_from_string_incorrect_case():
    assert Bounty("aBsEnCe Of MoSs").name == "absence of moss"


def test_init_from_none():
    assert Bounty(None).name == "none"


def test_init_from_default():
    assert Bounty().name == "none"


def test_init_invalid():
    with pytest.raises(ValueError):
        Bounty("")


def test_str():
    assert str(Bounty("absence of moss")) == "absence of moss"


def test_repr():
    assert repr(Bounty("absence of moss")) == "Bounty('absence of moss')"


def test_hash():
    assert hash(Bounty("absence of moss")) == hash("absence of moss")


def test_eq():
    assert Bounty("absence of moss") == Bounty("absence of moss")


def test_lt():
    assert Bounty("absence of moss") < Bounty("bean-shaped rock")


def test_bool_is_true():
    assert bool(Bounty("absence of moss"))


def test_bool_is_false():
    assert not bool(Bounty(None))


def test_all_are_unique():
    bounties = Bounty.all()
    assert len(set(bounties)) == len(bounties)


def test_all_are_serializable():
    bounties = Bounty.all()
    assert bounties == [Bounty(str(bounty)) for bounty in bounties]


def test_all_are_true():
    assert all(Bounty.all())


@pytest.mark.parametrize(
    "name",
    common.get_property_names(Bounty),
)
def test_property(name):
    getattr(Bounty("absence of moss"), name)
