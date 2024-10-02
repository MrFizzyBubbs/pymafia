from typing import Iterable as _Iterable

from jpype import JClass as _JClass

_jclass_names: dict[str, str] = {}


def __dir__() -> _Iterable[str]:
    return sorted(list(_jclass_names.keys()))


def __getattr__(name: str) -> _JClass:
    if name in _jclass_names:
        return _JClass(_jclass_names[name])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
