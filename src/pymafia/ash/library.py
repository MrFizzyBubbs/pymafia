from typing import Any

from jpype import JClass

from pymafia.ash.conversion import from_java, to_java
from pymafia.kolmafia import km

String = JClass("java.lang.String")
ByteArrayInputStream = JClass("java.io.ByteArrayInputStream")


class LibraryFunction:
    def __init__(self, name: str):
        self.name = name
        self.func = getattr(km.RuntimeLibrary, self.name)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name!r})"

    def __call__(self, *args, raw=False) -> Any:
        interpreter = km.AshRuntime()
        jargs = [to_java(arg) for arg in args]
        value = self.func(interpreter, *jargs)
        return value if raw else from_java(value)

    @property
    def signatures(self) -> list[str]:
        functions = km.RuntimeLibrary.getFunctions().findFunctions(self.name)
        return [f"{f.getType().toString()} {f.getSignature()}" for f in functions]


def script(lines: str, raw=False) -> Any:
    stream = ByteArrayInputStream(String(lines).getBytes())
    interpreter = km.AshRuntime()
    interpreter.validate(None, stream)
    value = interpreter.execute("main", None)
    return value if raw else from_java(value)


def ashref(command="") -> list[str]:
    names = set()
    for func in km.RuntimeLibrary.getFunctions():
        name = func.getName()
        if command.casefold() in name.casefold():
            names.add(name)
    return sorted(names)
