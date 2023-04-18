from __future__ import annotations

from dataclasses import dataclass

from pymafia.kolmafia import km


@dataclass(frozen=True, order=True)
class Slot:
    name: str = km.DataTypes.SLOT_INIT.contentString

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.name.casefold()
        ) or key is None:
            return

        slot = km.EquipmentRequest.slotNumber(key)
        if slot == km.Slot.NONE:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "name", slot.name)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Slot]:
        from pymafia.ash import from_java

        values = km.DataTypes.SLOT_TYPE.allValues()
        return from_java(values)
