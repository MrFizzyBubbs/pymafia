from typing import Any

from pymafia.ash.conversion import from_java, to_java
from pymafia.kolmafia import km


class LibraryFunction:
    def __init__(self, name: str):
        self.name = name
        self.function = getattr(km.RuntimeLibrary, self.name)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name!r})"

    def __call__(self, *args) -> Any:
        interpreter = km.AshRuntime()
        jargs = [to_java(arg) for arg in args]
        value = self.function(interpreter, *jargs)
        return from_java(value)
