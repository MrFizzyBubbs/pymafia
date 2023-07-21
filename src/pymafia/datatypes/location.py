from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, ClassVar

from jpype import JClass

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.bounty import Bounty

Integer = JClass("java.lang.Integer")


@dataclass(frozen=True, order=True)
class Location:
    NONE: ClassVar[Location]

    kol_adventure: Any = field(
        default=km.DataTypes.LOCATION_INIT.content, compare=False
    )
    id: int = -1  # LOCATION_INIT does not specify an id
    name: str = km.DataTypes.LOCATION_INIT.contentString

    def __init__(self, key: int | str | None = None):
        if (isinstance(key, str) and key.casefold() == self.name.casefold()) or key in (
            self.id,
            None,
        ):
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

        object.__setattr__(self, "kol_adventure", kol_adventure)
        object.__setattr__(self, "id", kol_adventure.getSnarfblat())
        object.__setattr__(self, "name", kol_adventure.getAdventureName())

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Location]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.LOCATION_TYPE.allValues()
        return sorted(from_java(values))

    @property
    def url(self) -> str:
        return f"adventure.php?snarfblat={self.id}"

    @property
    def nocombats(self) -> bool:
        return self.kol_adventure is not None and self.kol_adventure.isNonCombatsOnly()

    @property
    def combat_percent(self) -> float:
        if self.kol_adventure is None:
            return 0
        area = self.kol_adventure.getAreaSummary()
        return area.areaCombatPercent() if area is not None else 0

    @property
    def zone(self) -> str:
        return self.kol_adventure.getZone() if self.kol_adventure is not None else ""

    @property
    def parent(self) -> str:
        return (
            self.kol_adventure.getParentZone() if self.kol_adventure is not None else ""
        )

    @property
    def parentdesc(self) -> str:
        return (
            self.kol_adventure.getParentZoneDescription()
            if self.kol_adventure is not None
            else ""
        )

    @property
    def environment(self) -> str:
        return (
            self.kol_adventure.getEnvironment()
            if self.kol_adventure is not None
            else ""
        )

    @property
    def root(self) -> str:
        return (
            self.kol_adventure.getRootZone() if self.kol_adventure is not None else ""
        )

    @property
    def bounty(self) -> Bounty:
        from pymafia.datatypes.bounty import Bounty

        if self.kol_adventure is None:
            return Bounty()
        bounty = km.AdventureDatabase.getBounty(self.kol_adventure)
        return Bounty(bounty.getName()) if bounty is not None else Bounty()

    @property
    def combat_queue(self) -> list[str]:
        if self.kol_adventure is None:
            return []

        zone_queue = km.AdventureQueueDatabase.getZoneQueue(self.kol_adventure)
        return list(zone_queue) if zone_queue is not None else []

    @property
    def noncombat_queue(self) -> list[str]:
        if self.kol_adventure is None:
            return []
        zone_queue = km.AdventureQueueDatabase.getZoneNoncombatQueue(self.kol_adventure)
        return list(zone_queue) if zone_queue is not None else []

    @property
    def turns_spent(self) -> int:
        return (
            km.AdventureSpentDatabase.getTurns(self.kol_adventure, True)
            if self.kol_adventure is not None
            else 0
        )

    @property
    def kisses(self) -> int:
        return (
            km.FightRequest.dreadKisses(self.kol_adventure)
            if self.kol_adventure is not None
            else 0
        )

    @property
    def recommended_stat(self) -> int:
        return (
            self.kol_adventure.getRecommendedStat()
            if self.kol_adventure is not None
            else 0
        )

    @property
    def poison(self) -> int:
        if self.kol_adventure is None:
            return Integer.MAX_VALUE
        area = self.kol_adventure.getAreaSummary()
        return area.poison() if area is not None else Integer.MAX_VALUE

    @property
    def water_level(self) -> int:
        if self.kol_adventure is None or not km.KoLCharacter.inRaincore():
            return 0
        return self.kol_adventure.getWaterLevel()

    @property
    def wanderers(self) -> bool:
        return self.kol_adventure is not None and self.kol_adventure.hasWanderers()

    @property
    def fire_level(self) -> int:
        if self.kol_adventure is None or not km.KoLCharacter.inFirecore():
            return 0
        return km.WildfireCampRequest.getFireLevel(self.kol_adventure)


Location.NONE = Location()
