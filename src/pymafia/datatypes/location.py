import pymafia.kolmafia as km
from pymafia import ash, datatypes


class Location:
    id = -1
    name = "none"
    adventure = None

    def __init__(self, key=None):
        if key in (None, self.id, self.name):
            return

        adventure = (
            km.AdventureDatabase.getAdventure(key)
            if isinstance(key, str)
            else km.AdventureDatabase.getAdventureByURL(
                f"adventure.php?snarfblat={key}"
            )
        )

        if adventure is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = adventure.getSnarfblat()
        self.name = adventure.getAdventureName()
        self.adventure = adventure

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self):
        return hash((self.id, self.name))

    def __eq__(self, other):
        return isinstance(other, type(self)) and (self.id, self.name) == (
            other.id,
            other.name,
        )

    def __bool__(self):
        return (self.id, self.name) != (type(self).id, type(self).name)

    @classmethod
    def all(cls):
        values = km.DataTypes.LOCATION_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def url(self):
        return f"adventure.php?snarfblat={self.id}"

    @property
    def nocombats(self):
        return self.adventure.isNonCombatsOnly() if self else False

    @property
    def combat_percent(self):
        if not self:
            return 0
        area = self.adventure.getAreaSummary()
        return 0 if area is None else area.areaCombatPercent()

    @property
    def zone(self):
        return self.adventure.getZone() if self else ""

    @property
    def parent(self):
        return self.adventure.getParentZone() if self else ""

    @property
    def parentdesc(self):
        return self.adventure.getParentZoneDescription() if self else ""

    @property
    def environment(self):
        return self.adventure.getEnvironment() if self else ""

    @property
    def bounty(self):
        if not self:
            return None
        bounty = km.AdventureDatabase.getBounty(self.adventure)
        return None if bounty is None else datatypes.Bounty(bounty.getName())

    @property
    def combat_queue(self):
        if not self:
            return []
        zone_queue = km.AdventureQueueDatabase.getZoneQueue(self.adventure)
        return [] if zone_queue is None else list(zone_queue)

    @property
    def noncombat_queue(self):
        if not self:
            return []
        zone_queue = km.AdventureQueueDatabase.getZoneNoncombatQueue(self.adventure)
        return [] if zone_queue is None else list(zone_queue)

    @property
    def turns_spent(self):
        return km.AdventureSpentDatabase.getTurns(self.adventure, True) if self else 0

    @property
    def kisses(self):
        return km.FightRequest.dreadKisses(self.adventure) if self else 0

    @property
    def recommended_stat(self):
        return self.adventure.getRecommendedStat() if self else 0

    @property
    def water_level(self):
        return (
            self.adventure.getWaterLevel()
            if self and km.KoLCharacter.inRaincore()
            else 0
        )

    @property
    def wanderers(self):
        return self.adventure.hasWanderers() if self else False

    @property
    def fire_level(self):
        return (
            km.WildfireCampRequest.getFireLevel(self.adventure)
            if self and km.KoLCharacter.inFirecore()
            else 0
        )
