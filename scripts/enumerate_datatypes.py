import inspect
import sys

from pymafia.datatypes import *  # noqa: F403


def enumeration_name(string: str) -> str:
    result = string.split(":")[0].upper().replace(" ", "_").replace("-", "_")
    for char in [",", "!", "."]:
        result = result.replace(char, "")
    assert str.isidentifier(result), f"{result!r} is an invalid Python identifier"
    return result


def annotation(instance: type) -> str:
    return (
        f"    {enumeration_name(str(instance))}: ClassVar[{type(instance).__name__}]\n"
    )


def definition(instance: type) -> str:
    return f'{type(instance).__name__}.{enumeration_name(str(instance))} = {type(instance).__name__}("{str(instance)}")\n'


def sort_enumerations(cls):
    with open(f"./src/pymafia/datatypes/{cls.__name__.lower()}.py", "r") as f:
        lines = f.readlines()

    instances = [cls()] + cls.all()
    for func in [annotation, definition]:
        values = [func(x) for x in instances if func(x) in lines]
        indices = sorted(lines.index(x) for x in values)
        for index, value in zip(indices, values):
            lines[index] = value

    with open(f"./src/pymafia/datatypes/{cls.__name__.lower()}.py", "w") as f:
        f.writelines(lines)


def add_enumerations(cls):
    file = inspect.getfile(cls)
    with open(file, "r") as f:
        lines = f.readlines()

    instances = [cls()] + cls.all()
    missing = [x for x in instances if not hasattr(x, enumeration_name(str(x)))]

    if len(missing) == 0:
        return
    confirmation = input(f"Add {len(missing):,} enumerations to {file}? [y]/n: ")
    if confirmation not in ("y", ""):
        return

    for func in [annotation, definition]:
        for instance in missing:
            index = max(
                (lines.index(func(x)) for x in instances if func(x) in lines),
                lines.index(f"class {cls.__name__}"),
            )
            value = func(instance)
            lines.insert(index + 1, value)
            print(f"inserted {value!r} on line {index + 1}")


if __name__ == "__main__":
    class_name = sys.argv[1]
    cls = getattr(sys.modules[__name__], class_name)
    add_enumerations(cls)
