from enum import Enum
from functools import cached_property
from typing import Any


class LazyEnum(Enum):
    """A base class for enums with lazy evaluation of callable values.

    This class allows enum members to have callable values that are evaluated lazily
    (i.e., only when first accessed), and the result is cached by overwriting the
    original _value_ attribute with the evaluated result.

    Note that Enum members whose values are functions are considered method definitions
    instead of attributes. To work around this, functools.partial or a wrapper class can
    be used.
    """

    @classmethod
    def _missing_(cls, value: object) -> Any:
        for member in cls:
            if member.value == value:
                return member
        return None

    @cached_property
    def value(self) -> Any:
        if callable(self._value_):
            self._value_ = self._value_()
        return self._value_
