from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from ._bounty import Bounty


class Location:
    id: int = -1
    name: str = "none"
    adventure: Any = None

    def __init__(self, key: int | str | None = None):
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

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self) -> int:
        return hash((self.id, self.name))

    def __eq__(self, other) -> bool:
        return isinstance(other, type(self)) and (self.id, self.name) == (
            other.id,
            other.name,
        )

    def __bool__(self) -> bool:
        return (self.id, self.name) != (type(self).id, type(self).name)

    @classmethod
    def all(cls) -> list[Location]:
        from pymafia import ash

        values = km.DataTypes.LOCATION_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def url(self) -> str:
        return f"adventure.php?snarfblat={self.id}"

    @property
    def nocombats(self) -> bool:
        return self.adventure.isNonCombatsOnly() if self else False

    @property
    def combat_percent(self) -> float:
        if not self:
            return 0
        area = self.adventure.getAreaSummary()
        return 0 if area is None else area.areaCombatPercent()

    @property
    def zone(self) -> str:
        return self.adventure.getZone() if self else ""

    @property
    def parent(self) -> str:
        return self.adventure.getParentZone() if self else ""

    @property
    def parentdesc(self) -> str:
        return self.adventure.getParentZoneDescription() if self else ""

    @property
    def environment(self) -> str:
        return self.adventure.getEnvironment() if self else ""

    @property
    def bounty(self) -> Bounty:
        from ._bounty import Bounty

        if not self:
            return Bounty(None)
        bounty = km.AdventureDatabase.getBounty(self.adventure)
        return Bounty(None) if bounty is None else Bounty(bounty.getName())

    @property
    def combat_queue(self) -> list[str]:
        if not self:
            return []
        zone_queue = km.AdventureQueueDatabase.getZoneQueue(self.adventure)
        return [] if zone_queue is None else list(zone_queue)

    @property
    def noncombat_queue(self) -> list[str]:
        if not self:
            return []
        zone_queue = km.AdventureQueueDatabase.getZoneNoncombatQueue(self.adventure)
        return [] if zone_queue is None else list(zone_queue)

    @property
    def turns_spent(self) -> int:
        return km.AdventureSpentDatabase.getTurns(self.adventure, True) if self else 0

    @property
    def kisses(self) -> int:
        return km.FightRequest.dreadKisses(self.adventure) if self else 0

    @property
    def recommended_stat(self) -> int:
        return self.adventure.getRecommendedStat() if self else 0

    @property
    def poison(self) -> int:
        raise NotImplementedError

    @property
    def water_level(self) -> int:
        return (
            self.adventure.getWaterLevel()
            if self and km.KoLCharacter.inRaincore()
            else 0
        )

    @property
    def wanderers(self) -> bool:
        return self.adventure.hasWanderers() if self else False

    @property
    def fire_level(self) -> int:
        return (
            km.WildfireCampRequest.getFireLevel(self.adventure)
            if self and km.KoLCharacter.inFirecore()
            else 0
        )
