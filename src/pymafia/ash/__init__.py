__all__ = ["LibraryFunction", "from_java", "to_java"]

from typing import Any

from pymafia.ash.conversion import from_java, to_java
from pymafia.ash.library import LibraryFunction


def __getattr__(name: str) -> Any:
    return LibraryFunction(name)
