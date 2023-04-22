__all__ = ["LibraryFunction", "ashref", "script", "from_java", "to_java"]

from pymafia.ash.conversion import from_java, to_java
from pymafia.ash.library import LibraryFunction, ashref, script


def __getattr__(name: str) -> LibraryFunction:
    return LibraryFunction(name)
