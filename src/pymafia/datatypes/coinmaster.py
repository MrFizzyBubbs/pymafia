from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.item import Item


@dataclass(frozen=True, order=True)
class Coinmaster:
    name: str = "none"

    def __init__(self, key: str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.name.casefold()
        ) or key is None:
            return

        coinmaster = km.CoinmasterRegistry.findCoinmaster(key)
        if coinmaster is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "name", coinmaster.getMaster())

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self.name != type(self).name

    @classmethod
    def all(cls) -> list[Coinmaster]:
        from pymafia.ash import from_java

        values = km.DataTypes.COINMASTER_TYPE.allValues()
        return from_java(values)

    @property
    def coinmaster(self) -> Any:
        return km.CoinmasterRegistry.findCoinmaster(self.name)

    @property
    def token(self) -> str:
        return self.coinmaster.getToken() if self else ""

    @property
    def item(self) -> Item:
        from pymafia.datatypes.item import Item

        if not self:
            return Item(None)
        item = self.coinmaster.getItem()
        return Item(None) if item is None else Item(item.getItemId())

    @property
    def preference(self) -> str:
        return self.coinmaster.getProperty() if self else ""

    @property
    def available_tokens(self) -> int:
        return self.coinmaster.availableTokens() if self else 0

    @property
    def buys(self) -> bool:
        return self.coinmaster.getSellAction() is not None if self else False

    @property
    def sells(self) -> bool:
        return self.coinmaster.getBuyAction() is not None if self else False

    @property
    def nickname(self) -> str:
        return self.coinmaster.getNickname() if self else ""
