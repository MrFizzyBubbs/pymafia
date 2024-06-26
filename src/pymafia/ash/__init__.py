from pymafia.ash import library
from pymafia.ash.conversion import from_java, to_java
from pymafia.ash.function import LibraryFunction
from pymafia.ash.library import *

__all__ = library.__all__


def __getattr__(name: str) -> LibraryFunction:
    return LibraryFunction(name)
