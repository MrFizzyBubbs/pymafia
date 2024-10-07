from pymafia.ash import library
from pymafia.ash.conversion import from_java, to_java
from pymafia.ash.function import LibraryFunction
from pymafia.ash.library import *

__all__ = ["from_java", "to_java"]
__all__.extend(library.__all__)


def __getattr__(name: str) -> LibraryFunction:
    """Dynamically create a LibraryFunction for an unknown ASH function name.

    This ensures support for ASH functions added in KoLmafia revisions newer than what
    the package was released with.
    """
    return LibraryFunction(name)
