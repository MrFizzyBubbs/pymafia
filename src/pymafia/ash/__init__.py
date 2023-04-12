__all__ = ["LibraryFunction", "from_java", "to_java"]

from pymafia.ash.conversion import from_java, to_java
from pymafia.ash.library import LibraryFunction


def __getattr__(name: str) -> LibraryFunction:
    return LibraryFunction(name)
