from pymafia.kolmafia import km
from pymafia import ash


class Location:
    def __init__(self, key):
        if key in (None, -1, "none"):
            self.id = -1
            self.name = "none"
            return

        if isinstance(key, str):
            content = km.AdventureDatabase.getAdventure(key)
        else:
            content = km.AdventureDatabase.getAdventureByURL(
                f"adventure.php?snarfblat={key}"
            )

        if content is None:
            raise NameError(f"{type(self).__name__} {key!r} not found")

        self.id = content.getSnarfblat()
        self.name = content.getAdventureName()

    @classmethod
    def all(cls):
        values = km.DataTypes.LOCATION_TYPE.allValues()
        return sorted(ash.from_java(values), key=lambda x: x.id)

    def __hash__(self):
        return hash((self.id, self.name))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __eq__(self, other):
        return isinstance(other, type(self)) and (self.id, self.name) == (
            other.id,
            other.name,
        )

    def __bool__(self):
        return self.id != -1

    @property
    def url(self):
        return f"adventure.php?snarfblat={self.id}"

    @property
    def noncombat_queue(self):
        return km.AdventureQueueDatabase.getZoneNoncombatQueue(self.name).toArray()
