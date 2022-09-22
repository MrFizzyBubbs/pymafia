from typing import Any, Type, TypeVar, overload

from pymafia.kolmafia import km

T = TypeVar("T")


@overload
def get_property(name: str) -> str:
    ...


@overload
def get_property(name: str, t: Type[T]) -> T:
    ...


def get_property(name, t=str):
    """Return the value of a KoLmafia property."""
    if t is bool:
        return km.Preferences.getBoolean(name)
    if t is int:
        return km.Preferences.getInteger(name)
    if t is float:
        return km.Preferences.getFloat(name)
    return t(km.Preferences.getString(name))


def set_property(name: str, value: Any = ""):
    """Set the value of a KoLmafia property."""
    if isinstance(value, bool):
        km.Preferences.setBoolean(name, value)
    elif isinstance(value, int):
        km.Preferences.setInteger(name, value)
    elif isinstance(value, float):
        km.Preferences.setFloat(name, value)
    else:
        km.Preferences.setString(name, str(value))


def set_choice(choice: int, value: int | str):
    """Set the value of a KoLmafia choice adventure property."""
    set_property(f"choiceAdventure{choice}", value)
