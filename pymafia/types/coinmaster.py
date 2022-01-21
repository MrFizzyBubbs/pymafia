from pymafia.kolmafia import km
from pymafia import ash


class Coinmaster:
    def __init__(self, key):
        if key in (None, "none"):
            self.name = "none"
            return

        coinmaster_data = km.CoinmasterRegistry.findCoinmaster(key)

        if coinmaster_data is None:
            raise NameError(f"{type(self).__name__} {key!r} not found")

        self.name = coinmaster_data.getMaster()

    @classmethod
    def all(cls):
        values = km.DataTypes.COINMASTER_TYPE.allValues()
        return sorted(ash.from_java(values), key=lambda x: x.name)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.name == other.name

    def __bool__(self):
        return self.name != "none"
