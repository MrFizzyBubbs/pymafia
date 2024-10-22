"""Convert to and from Java KoLmafia Values.

References:
- https://github.com/kolmafia/kolmafia/blob/82a2030a7c0437fe39e1fccf33f856e7d0a37a26/src/net/sourceforge/kolmafia/textui/javascript/ValueConverter.java
- https://github.com/kolmafia/kolmafia/blob/82a2030a7c0437fe39e1fccf33f856e7d0a37a26/src/net/sourceforge/kolmafia/textui/javascript/ScriptableValueConverter.java#L17
"""

from collections import abc
from typing import Any

from jpype import JClass

from pymafia import datatypes
from pymafia.datatypes import (
    SPECIAL_DATATYPES,
    Matcher,
)
from pymafia.kolmafia import km


def check_valid_map_key(value: Any) -> None:
    """Check that the given value is a valid key type for an ASH map."""
    is_string = value.getType().equals(km.DataTypes.STRING_TYPE)
    is_int = value.getType().equals(km.DataTypes.INT_TYPE)
    is_enumerated = km.DataTypes.enumeratedTypes.contains(value.getType()) and (
        value.contentString.length() > 0 or value.contentLong > 0
    )
    if not (is_string or is_int or is_enumerated):
        raise TypeError(
            "Maps may only have keys of type string, int, or an enumerated type."
        )


def convert_python_mapping(mapping: abc.Mapping) -> Any:
    """Convert a Python mapping to a net.sourceforge.kolmafia.textui.MapValue."""
    if len(mapping) == 0:
        return km.MapValue(
            km.AggregateType(km.DataTypes.ANY_TYPE, km.DataTypes.ANY_TYPE)
        )

    first_key = next(iter(mapping.keys()))
    first_value = next(iter(mapping.values()))
    data_type = to_java(first_value).getType()
    index_type = to_java(first_key).getType()

    TreeMap = JClass("java.util.TreeMap")
    underlying_map = TreeMap()
    for key, value in mapping.items():
        jkey = to_java(key)
        jvalue = to_java(value)
        check_valid_map_key(jkey)
        underlying_map.put(jkey, jvalue)
    return km.MapValue(km.AggregateType(data_type, index_type), underlying_map)


def convert_python_sequence(sequence: abc.Sequence) -> Any:
    """Convert a Python sequence to a net.sourceforge.kolmafia.textui.ArrayValue."""
    if len(sequence) == 0:
        return km.ArrayValue(km.AggregateType(km.DataTypes.ANY_TYPE, 0))

    first_element = to_java(sequence[0])
    element_type = first_element.getType()

    ArrayList = JClass("java.util.ArrayList")
    result = ArrayList()
    for element in sequence:
        result.add(to_java(element))
    return km.ArrayValue(km.AggregateType(element_type, len(sequence)), result)


def to_java(obj: Any) -> Any:
    """Convert a Python object to a net.sourceforge.kolmafia.textui.Value."""
    if obj is None:
        return km.Value()
    if isinstance(obj, bool):
        return km.DataTypes.makeBooleanValue(obj)
    if isinstance(obj, int):
        return km.DataTypes.makeIntValue(obj)
    if isinstance(obj, float):
        return km.DataTypes.makeFloatValue(obj)
    if isinstance(obj, str):
        return km.DataTypes.makeStringValue(obj)
    if isinstance(obj, abc.Mapping):
        return convert_python_mapping(obj)
    if isinstance(obj, abc.Sequence):
        return convert_python_sequence(obj)
    if isinstance(obj, SPECIAL_DATATYPES):
        parser = getattr(km.DataTypes, f"parse{type(obj).__name__}Value")
        return parser(str(obj), False)
    if isinstance(obj, Matcher):
        return km.Value(
            km.DataTypes.MATCHER_TYPE, obj.pattern().toString(), obj.__wrapped__
        )
    raise TypeError(f"{type(obj).__name__!r}")


def from_java(obj: Any) -> Any:
    """Convert a net.sourceforge.kolmafia.textui.Value to a Python object."""
    jtype = obj.getType()
    if jtype == km.DataTypes.VOID_TYPE:
        return None
    if jtype == km.DataTypes.BOOLEAN_TYPE:
        return obj.contentLong != 0
    if jtype == km.DataTypes.INT_TYPE:
        return obj.contentLong
    if jtype == km.DataTypes.FLOAT_TYPE:
        return obj.floatValue()
    if jtype in (km.DataTypes.STRING_TYPE, km.DataTypes.STRICT_STRING_TYPE):
        return obj.contentString
    if jtype == km.DataTypes.BUFFER_TYPE:
        return obj.content.toString()
    if jtype == km.DataTypes.MATCHER_TYPE:
        return Matcher(obj.rawValue())
    if isinstance(obj, km.MapValue):
        result = {}
        for key in obj.keys():
            value = obj.aref(key)
            result[from_java(key)] = from_java(value)
        return result
    if isinstance(obj, (km.ArrayValue, km.PluralValue)):
        return [from_java(value) for value in obj.content]
    if isinstance(obj, km.RecordValue):
        names = list(obj.getRecordType().getFieldNames())
        values = [from_java(f) for f in obj.getRecordFields()]
        return dict(zip(names, values))
    if isinstance(obj.asProxy(), km.RecordValue):
        class_name = jtype.toString().capitalize()
        cls = getattr(datatypes, class_name)
        return cls(obj.toString())
    raise TypeError(f"{jtype!r} (name={jtype.getName()!r})")
