import pytest

from pymafia.datatypes import Element
from tests import common


def test_init_from_string():
    assert Element("cold").name == "cold"


def test_init_from_string_incorrect_case():
    assert Element("cOlD").name == "cold"


def test_init_from_none():
    assert Element(None).name == "none"


def test_init_from_default():
    assert Element().name == "none"


def test_init_invalid():
    with pytest.raises(ValueError):
        Element("")


def test_str():
    assert str(Element("cold")) == "cold"


def test_repr():
    assert repr(Element("cold")) == "Element('cold')"


def test_hash():
    assert hash(Element("cold")) == hash("cold")


def test_eq():
    assert Element("cold") == Element("cold")


def test_lt():
    assert Element("cold") < Element("hot")


def test_bool_is_true():
    assert bool(Element("cold"))


def test_bool_is_false():
    assert not bool(Element(None))


def test_all_are_unique():
    elements = Element.all()
    assert len(set(elements)) == len(elements)


def test_all_are_serializable():
    elements = Element.all()
    assert elements == [Element(str(element)) for element in elements]


def test_all_are_true():
    assert all(Element.all())


@pytest.mark.parametrize(
    "name",
    common.get_property_names(Element),
)
def test_property(name):
    getattr(Element("cold"), name)
