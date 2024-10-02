from typing import Any as _Any
from typing import Iterable as _Iterable

from jpype import JClass as _JClass

_jclasses = {}


def __dir__() -> _Iterable[str]:
    global _jclasses
    return sorted(list(_jclasses.keys()))


def __getattr__(name: str) -> _Any:
    global _jclasses
    if name in _jclasses:
        return _JClass(_jclasses[name])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
