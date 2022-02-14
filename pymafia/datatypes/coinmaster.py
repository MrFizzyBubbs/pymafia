import pymafia.kolmafia as km
from pymafia import ash, datatypes


class Coinmaster:
    name = "none"
    coinmaster = None

    def __init__(self, key=None):
        if key in (None, self.name):
            return

        coinmaster = km.CoinmasterRegistry.findCoinmaster(key)

        if coinmaster is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.name = coinmaster.getMaster()
        self.coinmaster = coinmaster

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.name == other.name

    def __bool__(self):
        return self.name != type(self).name

    @classmethod
    def all(cls):
        values = km.DataTypes.COINMASTER_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.name)

    @property
    def token(self):
        return self.coinmaster.getToken() if self else None

    @property
    def item(self):
        if not self:
            return None
        item = self.coinmaster.getItem()
        return None if item is None else datatypes.Item(item.getItemId())

    @property
    def property_(self):
        return self.coinmaster.getProperty() if self else None

    @property
    def available_tokens(self):
        return self.coinmaster.availableTokens() if self else 0

    @property
    def buys(self):
        return self.coinmaster.getSellAction() is not None if self else False

    @property
    def sells(self):
        return self.coinmaster.getBuyAction() is not None if self else False

    @property
    def nickname(self):
        return self.coinmaster.getNickname() if self else None
