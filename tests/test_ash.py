import jpype
import pytest

from pymafia.ash.conversion import from_java, to_java
from pymafia.ash.library import git_info
from pymafia.datatypes import SPECIAL_DATATYPES, Matcher
from pymafia.kolmafia import km

JPattern = jpype.JClass("java.util.regex.Pattern")


@pytest.mark.parametrize(
    "value",
    [True, 1, 1.0, "1", {"a": 1, "b": 2}, [1, 2]]
    + [cls() for cls in SPECIAL_DATATYPES],
)
def test_java_conversion(value):
    assert from_java(to_java(value)) == value


def test_void_java_conversion():
    assert from_java(km.Value()) is None


def test_matcher_java_conversion():
    matcher = Matcher(JPattern.compile("(\\d)").matcher("0"))
    assert from_java(to_java(matcher)).__wrapped__ == matcher.__wrapped__


def test_record_java_conversion():
    assert git_info("") == {
        "url": "",
        "branch": "",
        "commit": "",
        "last_changed_author": "",
        "last_changed_date": "",
    }
