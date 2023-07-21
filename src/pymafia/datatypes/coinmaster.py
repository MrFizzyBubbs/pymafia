from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, ClassVar

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.item import Item


@dataclass(frozen=True, order=True)
class Coinmaster:
    NONE: ClassVar[Coinmaster]

    coinmaster: Any = field(default=km.DataTypes.COINMASTER_INIT.content, compare=False)
    name: str = km.DataTypes.COINMASTER_INIT.contentString

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.name.casefold()
        ) or key is None:
            return

        coinmaster = km.CoinmasterRegistry.findCoinmaster(key)
        if coinmaster is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "coinmaster", coinmaster)
        object.__setattr__(self, "name", coinmaster.getMaster())

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Coinmaster]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.COINMASTER_TYPE.allValues()
        return from_java(values)

    @property
    def token(self) -> str:
        return self.coinmaster.getToken() if self.coinmaster else ""

    @property
    def item(self) -> Item:
        from pymafia.datatypes.item import Item

        if self.coinmaster is None:
            return Item()
        item = self.coinmaster.getItem()
        return Item(item.getItemId()) if item is not None else Item()

    @property
    def preference(self) -> str:
        return self.coinmaster.getProperty() if self.coinmaster is not None else ""

    @property
    def available_tokens(self) -> int:
        return self.coinmaster.availableTokens() if self.coinmaster is not None else 0

    @property
    def buys(self) -> bool:
        return (
            self.coinmaster is not None and self.coinmaster.getSellAction() is not None
        )

    @property
    def sells(self) -> bool:
        return (
            self.coinmaster is not None and self.coinmaster.getBuyAction() is not None
        )

    @property
    def nickname(self) -> str:
        return self.coinmaster.getNickname() if self.coinmaster is not None else ""


Coinmaster.NONE = Coinmaster()
