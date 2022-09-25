from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from .item import Item


@total_ordering
class Coinmaster:
    name: str = "none"
    coinmaster: Any = None

    def __init__(self, key: str | None = None):
        if key in (None, self.name):
            return

        coinmaster = km.CoinmasterRegistry.findCoinmaster(key)
        if coinmaster is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.name = coinmaster.getMaster()
        self.coinmaster = coinmaster

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.name == other.name
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.name < other.name
        return NotImplemented

    def __bool__(self) -> bool:
        return self.name != type(self).name

    @classmethod
    def all(cls) -> list[Coinmaster]:
        from pymafia import ash

        values = km.DataTypes.COINMASTER_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def token(self) -> str:
        return self.coinmaster.getToken() if self else ""

    @property
    def item(self) -> Item:
        from .item import Item

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
