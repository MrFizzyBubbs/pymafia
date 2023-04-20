import pytest

from pymafia.ash import from_java, to_java
from pymafia.datatypes import MAFIA_DATATYPES
from pymafia.kolmafia import km


@pytest.mark.parametrize(
    "value",
    [True, 1, 1.0, "1", {"a": 1, "b": 2}, [1, 2]] + [cls() for cls in MAFIA_DATATYPES],
)
def test_java_conversion(value):
    assert from_java(to_java(value)) == value


def test_void_java_conversion():
    assert from_java(km.Value()) is not None
