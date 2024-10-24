import jpype
import pytest

from pymafia import datatypes
from pymafia.ash import from_java, to_java
from pymafia.datatypes import Matcher
from pymafia.kolmafia import km


def check_conversions(java_value, python_value):
    assert from_java(java_value) == python_value
    assert to_java(python_value).equals(java_value)


def test_void_conversion():
    check_conversions(km.Value(), None)


def test_boolean_conversion():
    check_conversions(km.DataTypes.makeBooleanValue(True), True)
    check_conversions(km.DataTypes.makeBooleanValue(False), False)


def test_int_conversion():
    check_conversions(km.DataTypes.makeIntValue(123), 123)


def test_float_conversion():
    check_conversions(km.DataTypes.makeFloatValue(3.14), 3.14)


def test_string_conversion():
    check_conversions(km.DataTypes.makeStringValue("Hello World"), "Hello World")


def test_strict_string_conversion():
    check_conversions(
        km.Value(km.DataTypes.STRICT_STRING_TYPE, "Strict Hello"), "Strict Hello"
    )


def test_buffer_conversion():
    StringBuffer = jpype.JClass("java.lang.StringBuffer")
    jvalue = km.Value(km.DataTypes.BUFFER_TYPE, "", StringBuffer("Buffer Content"))
    check_conversions(jvalue, "Buffer Content")


def test_matcher_conversion():
    Pattern = jpype.JClass("java.util.regex.Pattern")
    jmatcher = Pattern.compile("(\\d)").matcher("0")
    jvalue = km.Value(km.DataTypes.MATCHER_TYPE, "(\\d)", jmatcher)
    check_conversions(jvalue, Matcher(jmatcher))


def test_map_conversion():
    Map = jpype.JClass("java.util.Map")
    jmap = Map.of(
        km.DataTypes.makeStringValue("a"),
        km.DataTypes.makeIntValue(1),
        km.DataTypes.makeStringValue("b"),
        km.DataTypes.makeIntValue(2),
    )
    jvalue = km.MapValue(km.DataTypes.STRING_TO_INT_TYPE, jmap)
    check_conversions(jvalue, {"b": 2, "a": 1})


def test_map_conversion_with_invalid_key():
    with pytest.raises(TypeError):
        to_java({("a",): 1})


def test_array_conversion():
    List = jpype.JClass("java.util.List")
    jlist = List.of(["a", "b", "d"])
    java_value = km.DataTypes.makeStringArrayValue(jlist)
    check_conversions(java_value, ["a", "b", "d"])


def test_record_conversion():
    jarray = jpype.JArray(km.Value, 1)(
        [km.DataTypes.makeIntValue(1), km.DataTypes.makeStringValue("c")]
    )
    jvalue = km.RecordValue(
        km.RecordType(
            "test", ["a", "b"], [km.DataTypes.INT_TYPE, km.DataTypes.STRING_TYPE]
        )
    )
    jvalue.content = jarray
    # Only check from_java, to_java does not return a RecordValue for a dictionary object.
    assert from_java(jvalue) == {"a": 1, "b": "c"}


@pytest.mark.parametrize("jtype", km.DataTypes.enumeratedTypes)
def test_enumerated_conversion(jtype):
    jvalue = jtype.initialValue()
    cls = getattr(datatypes, jtype.getName().capitalize())
    check_conversions(jvalue, cls())
