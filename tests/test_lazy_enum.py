from functools import partial

import pytest

from pymafia.lazy_enum import LazyEnum


@pytest.fixture
def sample_lazy_enum():
    class SampleLazyEnum(LazyEnum):
        ONE = 1
        TWO = partial(lambda: 2)

    return SampleLazyEnum


def test_lookup_by_value(sample_lazy_enum):
    assert sample_lazy_enum(1) == sample_lazy_enum.ONE
    assert sample_lazy_enum(2) == sample_lazy_enum.TWO


def test_value_property(sample_lazy_enum):
    assert sample_lazy_enum.ONE.value == 1
    assert sample_lazy_enum.TWO.value == 2


def test_repr(sample_lazy_enum):
    assert repr(sample_lazy_enum.ONE) == "<SampleLazyEnum.ONE: 1>"

    assert repr(sample_lazy_enum.TWO).startswith(
        "<SampleLazyEnum.TWO: functools.partial("
    )
    sample_lazy_enum.TWO.value  # Access value to execute callable
    assert repr(sample_lazy_enum.TWO) == "<SampleLazyEnum.TWO: 2>"
