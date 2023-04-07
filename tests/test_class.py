import pytest

from pymafia.datatypes import Class
from tests import common


def test_init_from_int():
    class_ = Class(1)
    assert (class_.id, class_.name) == (1, "Seal Clubber")


def test_init_from_string():
    class_ = Class("Seal Clubber")
    assert (class_.id, class_.name) == (1, "Seal Clubber")


def test_init_from_string_incorrect_case():
    class_ = Class("sEaL cLuBbEr")
    assert (class_.id, class_.name) == (1, "Seal Clubber")


def test_init_from_none():
    class_ = Class(None)
    assert (class_.id, class_.name) == (-1, "none")


def test_init_from_default():
    class_ = Class()
    assert (class_.id, class_.name) == (-1, "none")


def test_init_invalid():
    with pytest.raises(ValueError):
        Class("")


def test_str():
    assert str(Class("Seal Clubber")) == "Seal Clubber"


def test_repr():
    assert repr(Class("Seal Clubber")) == "Class('Seal Clubber')"


def test_hash():
    assert hash(Class("Seal Clubber")) == hash((1, "Seal Clubber"))


def test_eq():
    assert Class(1) == Class(1)


def test_lt():
    assert Class(1) < Class(2)


def test_bool_is_true():
    assert bool(Class(1))


def test_bool_is_false():
    assert not bool(Class(None))


def test_all_are_unique():
    classes = Class.all()
    assert len(set(classes)) == len(classes)


def test_all_are_serializable():
    classes = Class.all()
    assert classes == [Class(str(class_)) for class_ in classes]


def test_all_are_true():
    assert all(Class.all())


@pytest.mark.parametrize(
    "name",
    common.get_property_names(Class),
)
def test_property(name):
    getattr(Class(1), name)
