from enum import Enum


class LazyEnum(Enum):
    """A base class for enums with lazy evaluation of callable values.

    This class allows enum members to have callable values that are evaluated lazily
    (i.e., only when first accessed), and the result is cached by overwriting the
    original _value_ attribute with the evaluated result. Overwriting _value_ is done so
    that member lookups by value (e.g., MyEnum('x')) function as expected. This could be
    improved by subclassing EnumMeta and defining a custom __call__.

    Note that Enum members whose values are functions are considered method definitions
    instead of attributes. To work around this, functools.partial or a wrapper class can
    be used.
    """

    def __getattribute__(self, name):
        result = super().__getattribute__(name)
        if name == "value":
            if callable(result):
                result = result()
                setattr(self, "_value_", result)
                return result
        return result
