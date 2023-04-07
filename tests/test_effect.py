import pytest

from pymafia.datatypes import Effect
from tests import common


def test_init_from_int():
    effect = Effect(1)
    assert (effect.id, effect.name) == (1, "Light!")


def test_init_from_string():
    effect = Effect("Light!")
    assert (effect.id, effect.name) == (1, "Light!")


def test_init_from_string_incorrect_case():
    effect = Effect("lIgHt!")
    assert (effect.id, effect.name) == (1, "Light!")


def test_init_from_none():
    effect = Effect(None)
    assert (effect.id, effect.name) == (-1, "none")


def test_init_from_default():
    effect = Effect()
    assert (effect.id, effect.name) == (-1, "none")


def test_init_invalid():
    with pytest.raises(ValueError):
        Effect("")


def test_str_for_unique_name():
    assert str(Effect("Light!")) == "Light!"


def test_str_for_non_unique_name():
    assert str(Effect("[800]Chocolate Reign")) == "[800]Chocolate Reign"


def test_repr():
    assert repr(Effect("Light!")) == "Effect('Light!')"


def test_hash():
    assert hash(Effect("Light!")) == hash((1, "Light!"))


def test_eq():
    assert Effect(1) == Effect(1)


def test_lt():
    assert Effect(1) < Effect(2)


def test_bool_is_true():
    assert bool(Effect(1))


def test_bool_is_false():
    assert not bool(Effect(None))


def test_all_are_unique():
    effects = Effect.all()
    assert len(set(effects)) == len(effects)


def test_all_are_serializable():
    effects = Effect.all()
    assert effects == [Effect(str(effect)) for effect in effects]


def test_all_are_true():
    assert all(Effect.all())


@pytest.mark.parametrize(
    "name",
    common.get_property_names(Effect),
)
def test_property(name):
    getattr(Effect(1), name)
