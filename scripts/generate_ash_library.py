from pathlib import Path
from typing import Any

from pymafia import datatypes
from pymafia.kolmafia import km
from pymafia.kolmafia.startup import start_kolmafia


def annotate(jtype: Any) -> str:
    # __eq__ does not work as expected for ANY_TYPE, use `.equals()` instead.
    if jtype.equals(km.DataTypes.ANY_TYPE):
        return "Any"
    if jtype == km.DataTypes.VOID_TYPE:
        return "None"
    if jtype == km.DataTypes.BOOLEAN_TYPE:
        return "bool"
    if jtype == km.DataTypes.INT_TYPE:
        return "int"
    if jtype == km.DataTypes.FLOAT_TYPE:
        return "float"
    if jtype in (
        km.DataTypes.STRING_TYPE,
        km.DataTypes.STRICT_STRING_TYPE,
        km.DataTypes.BUFFER_TYPE,
    ):
        return "str"
    if jtype == km.DataTypes.MATCHER_TYPE:
        return "Matcher"
    if isinstance(jtype, km.RecordType):
        return "dict[str, Any]"
    if isinstance(jtype, km.AggregateType):
        key_type = annotate(jtype.getIndexType())
        value_type = annotate(jtype.getDataType())
        return f"dict[{key_type}, {value_type}]"
    # Handle cases like `clear(aggregate)`, whose argument is not an instance of AggregateType.
    if jtype == km.DataTypes.AGGREGATE_TYPE:
        return "dict[Any, Any]"
    if isinstance(jtype.asProxy(), km.RecordType):
        return jtype.getName().capitalize()
    raise ValueError(jtype.toString())


def generate_overload(function: Any) -> list[str]:
    arg_names = function.getParameterNames()
    arg_types = [annotate(vr.getType()) for vr in function.getVariableReferences()]
    signature = ", ".join(": ".join(x) for x in zip(arg_names, arg_types))
    return_type = annotate(function.getType())
    return [
        "",
        "@overload",
        f"def {function.name}({signature}) -> {return_type}: ...",
        "",
    ]


def generate_implementation(function: Any, explicit: bool) -> list[str]:
    function_name = function.getName()
    if not explicit:
        return [
            "",
            f"def {function_name}(*args):",
            f'\treturn LibraryFunction("{function_name}")(*args)',
            "",
        ]

    arg_names = function.getParameterNames()
    arg_types = [annotate(vr.getType()) for vr in function.getVariableReferences()]
    signature = ", ".join(": ".join(x) for x in zip(arg_names, arg_types))
    return_type = annotate(function.getType())
    return [
        "",
        f"def {function_name}({signature}) -> {return_type}:",
        f'\treturn LibraryFunction("{function_name}")({", ".join(arg_names)})',
        "",
    ]


def generate_ash_library(path: str) -> None:
    start_kolmafia()

    function_names = sorted(
        {func.getName() for func in km.RuntimeLibrary.getFunctions()}
    )
    lines = [
        '"""Automatically generated Python implementations of KoLmafia\'s ASH functions.',
        "",
        f"See `scripts/{Path(__file__).name}` for more information.",
        '"""',
        f'__all__ = [{", ".join(repr(name) for name in function_names)}]',
        "",
        "from typing import Any, overload",
        "",
        "from pymafia.ash.function import LibraryFunction",
        f'from pymafia.datatypes import {", ".join(sorted(cls.__name__ for cls in datatypes.SPECIAL_DATATYPES))}, Matcher',
        "",
    ]

    for name in function_names:
        functions = km.RuntimeLibrary.getFunctions().findFunctions(name)[::-1]
        if len(functions) == 1:
            lines += generate_implementation(functions[0], explicit=True)
        else:
            for function in functions:
                lines += generate_overload(function)
            lines += generate_implementation(function, explicit=False)

    with open(path, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    generate_ash_library("./src/pymafia/ash/library.py")
