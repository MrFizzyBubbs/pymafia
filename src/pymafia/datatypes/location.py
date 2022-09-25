from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from .bounty import Bounty


Integer = km.autoclass("java.lang.Integer")


@total_ordering
class Location:
    id: int = -1
    name: str = "none"
    kol_adventure: Any = None

    def __init__(self, key: int | str | None = None):
        if key in (None, self.name, self.id):
            return

        kol_adventure = (
            km.AdventureDatabase.getAdventure(key)
            if isinstance(key, str)
            else km.AdventureDatabase.getAdventureByURL(
                f"adventure.php?snarfblat={key}"
            )
        )
        if kol_adventure is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = kol_adventure.getSnarfblat()
        self.name = kol_adventure.getAdventureName()
        self.kol_adventure = kol_adventure

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id == other.id
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id < other.id
        return NotImplemented

    def __bool__(self) -> bool:
        return self.id != type(self).id

    @classmethod
    def all(cls) -> list[Location]:
        from pymafia import ash

        values = km.DataTypes.LOCATION_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def url(self) -> str:
        return f"adventure.php?snarfblat={self.id}"

    @property
    def nocombats(self) -> bool:
        return self.kol_adventure.isNonCombatsOnly() if self else False

    @property
    def combat_percent(self) -> float:
        if not self:
            return 0
        area = self.kol_adventure.getAreaSummary()
        return 0 if area is None else area.areaCombatPercent()

    @property
    def zone(self) -> str:
        return self.kol_adventure.getZone() if self else ""

    @property
    def parent(self) -> str:
        return self.kol_adventure.getParentZone() if self else ""

    @property
    def parentdesc(self) -> str:
        return self.kol_adventure.getParentZoneDescription() if self else ""

    @property
    def environment(self) -> str:
        return self.kol_adventure.getEnvironment() if self else ""

    @property
    def bounty(self) -> Bounty:
        from .bounty import Bounty

        if not self:
            return Bounty(None)
        bounty = km.AdventureDatabase.getBounty(self.kol_adventure)
        return Bounty(None) if bounty is None else Bounty(bounty.getName())

    @property
    def combat_queue(self) -> list[str]:
        if not self:
            return []
        zone_queue = km.AdventureQueueDatabase.getZoneQueue(self.kol_adventure)
        return [] if zone_queue is None else list(zone_queue)

    @property
    def noncombat_queue(self) -> list[str]:
        if not self:
            return []
        zone_queue = km.AdventureQueueDatabase.getZoneNoncombatQueue(self.kol_adventure)
        return [] if zone_queue is None else list(zone_queue)

    @property
    def turns_spent(self) -> int:
        return (
            km.AdventureSpentDatabase.getTurns(self.kol_adventure, True) if self else 0
        )

    @property
    def kisses(self) -> int:
        return km.FightRequest.dreadKisses(self.kol_adventure) if self else 0

    @property
    def recommended_stat(self) -> int:
        return self.kol_adventure.getRecommendedStat() if self else 0

    @property
    def poison(self) -> int:
        if not self:
            return Integer.MAX_VALUE
        area = self.kol_adventure.getAreaSummary()
        return Integer.MAX_VALUE if area is None else area.poison()

    @property
    def water_level(self) -> int:
        return (
            self.kol_adventure.getWaterLevel()
            if self and km.KoLCharacter.inRaincore()
            else 0
        )

    @property
    def wanderers(self) -> bool:
        return self.kol_adventure.hasWanderers() if self else False

    @property
    def fire_level(self) -> int:
        return (
            km.WildfireCampRequest.getFireLevel(self.kol_adventure)
            if self and km.KoLCharacter.inFirecore()
            else 0
        )
