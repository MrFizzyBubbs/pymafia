from enum import Enum
from functools import cached_property
from typing import Any


class LazyEnum(Enum):
    """A base class for enums with lazy evaluation of callable values.

    This class allows enum members to have values that are evaluated lazily (i.e., only
    when first accessed). If a member's value is a callable, it will be evaluated and
    cached the first time the `value` property is accessed. The evaluated result
    replaces the original `_value_` attribute, which ensures that it is reflected in the
    `__repr__` output. Additionally, the `_missing_` class method ensures that members
    whose value is a callable can be looked up by the evaluted value.

    Note that enum members whose values are callables are considered method definitions
    instead of attributes. To avoid this behavior, use `functools.partial`, a wrapper
    class, or the `enum.member` decorator added in Python 3.11.
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
