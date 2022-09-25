from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from .item import Item


@total_ordering
class Familiar:
    id: int = -1
    name: str = "none"

    def __init__(self, key: int | str | None = None):
        if key in (None, self.name, self.id):
            return

        id = km.FamiliarDatabase.getFamiliarId(key) if isinstance(key, str) else key
        name = km.FamiliarDatabase.getFamiliarName(id)
        if name is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = id
        self.name = name

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
    def all(cls) -> list[Familiar]:
        from pymafia import ash

        values = km.DataTypes.FAMILIAR_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def hatchling(self) -> Item:
        from .item import Item

        return Item(km.FamiliarDatabase.getFamiliarLarva(self.id))

    @property
    def image(self) -> str:
        return km.FamiliarDatabase.getFamiliarImageLocation(self.id)

    @property
    def nickname(self) -> str:
        fam = km.KoLCharacter.ownedFamiliar(self.name)
        return fam.getName() if fam.isPresent() else ""

    @property
    def owner(self) -> str:
        fam = km.KoLCharacter.ownedFamiliar(self.name)
        return fam.getOwner() if fam.isPresent() else ""

    @property
    def owner_id(self) -> int:
        fam = km.KoLCharacter.ownedFamiliar(self.name)
        return fam.getOwnderId() if fam.isPresent() else 0

    @property
    def experience(self) -> int:
        fam = km.KoLCharacter.usableFamiliar(self.id)
        return fam.getTotalExperience() if fam is not None else 0

    @property
    def charges(self) -> int:
        fam = km.KoLCharacter.usableFamiliar(self.id)
        return fam.getCharges() if fam is not None else 0

    @property
    def drop_name(self) -> str:
        return km.FamiliarData.dropName(self.id) or ""

    @property
    def drop_item(self) -> Item:
        from .item import Item

        item = km.FamiliarData.dropItem(self.id)
        return Item(item.getItemId() if item is not None else None)

    @property
    def drops_today(self) -> int:
        return km.FamiliarData.dropsToday(self.id)

    @property
    def drops_limit(self) -> int:
        return km.FamiliarData.dropsToday(self.id)

    @property
    def fights_today(self) -> int:
        return km.FamiliarData.fightsToday(self.id)

    @property
    def fights_limit(self) -> int:
        return km.FamiliarData.fightDailyCap(self.id)

    @property
    def combat(self) -> bool:
        return km.FamiliarDatabase.isCombatType(self.id)

    @property
    def physical_damage(self) -> bool:
        return km.FamiliarDatabase.isCombat0Type(self.id)

    @property
    def elemental_damage(self) -> bool:
        return km.FamiliarDatabase.isCombat1Type(self.id)

    @property
    def block(self) -> bool:
        return km.FamiliarDatabase.isBlockType(self.id)

    @property
    def delevel(self) -> bool:
        return km.FamiliarDatabase.isDelevelType(self.id)

    @property
    def hp_during_combat(self) -> bool:
        return km.FamiliarDatabase.isHp0Type(self.id)

    @property
    def mp_during_combat(self) -> bool:
        return km.FamiliarDatabase.isMp0Type(self.id)

    @property
    def other_action_during_combat(self) -> bool:
        return km.FamiliarDatabase.isOther0Type(self.id)

    @property
    def hp_after_combat(self) -> bool:
        return km.FamiliarDatabase.isHp1Type(self.id)

    @property
    def mp_after_combat(self) -> bool:
        return km.FamiliarDatabase.isMp1Type(self.id)

    @property
    def other_action_after_combat(self) -> bool:
        return km.FamiliarDatabase.isOther1Type(self.id)

    @property
    def passive(self) -> bool:
        return km.FamiliarDatabase.isPassiveType(self.id)

    @property
    def underwater(self) -> bool:
        return km.FamiliarDatabase.isUnderwaterType(self.id)

    @property
    def variable(self) -> bool:
        return km.FamiliarDatabase.isVariableType(self.id)

    @property
    def attributes(self) -> list[str]:
        attrs = km.FamiliarDatabase.getFamiliarAttributes(self.id)
        return [] if attrs is None else list(attrs)

    @property
    def poke_level(self) -> int:
        fam = km.KoLCharacter.usableFamiliar(self.id)
        return 0 if fam is None else fam.getPokeLevel()

    @property
    def poke_level_2_power(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getPower2()

    @property
    def poke_level_2_hp(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getHP2()

    @property
    def poke_level_3_power(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getPower3()

    @property
    def poke_level_3_hp(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getHP3()

    @property
    def poke_level_4_power(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getPower4()

    @property
    def poke_level_4_hp(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getHP4()

    @property
    def poke_move_1(self) -> str:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return "" if data is None else data.getMove1()

    @property
    def poke_move_2(self) -> str:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return "" if data is None else data.getMove2()

    @property
    def poke_move_3(self) -> str:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return "" if data is None else data.getMove3()

    @property
    def poke_attribute(self) -> str:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return "" if data is None else data.getAttribute()
