from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.item import Item


@dataclass(frozen=True, order=True)
class Familiar:
    NONE: ClassVar[Familiar]

    id: int = km.DataTypes.FAMILIAR_INIT.contentLong
    name: str = km.DataTypes.FAMILIAR_INIT.contentString

    def __init__(self, key: int | str | None = None):
        if (isinstance(key, str) and key.casefold() == self.name.casefold()) or key in (
            self.id,
            None,
        ):
            return

        id = km.FamiliarDatabase.getFamiliarId(key) if isinstance(key, str) else key
        name = km.FamiliarDatabase.getFamiliarName(id)
        if name is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "id", id)
        object.__setattr__(self, "name", name)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Familiar]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.FAMILIAR_TYPE.allValues()
        return sorted(from_java(values))

    @property
    def hatchling(self) -> Item:
        from pymafia.datatypes.item import Item

        try:
            return Item(km.FamiliarDatabase.getFamiliarLarva(self.id))
        except ValueError:
            return Item()

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
        from pymafia.datatypes.item import Item

        item = km.FamiliarData.dropItem(self.id)
        return Item(item.getItemId()) if item is not None else Item()

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
        return list(attrs) if attrs is not None else []

    @property
    def poke_level(self) -> int:
        fam = km.KoLCharacter.usableFamiliar(self.id)
        return fam.getPokeLevel() if fam is not None else 0

    @property
    def poke_level_2_power(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return data.getPower2() if data is not None else 0

    @property
    def poke_level_2_hp(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return data.getHP2() if data is not None else 0

    @property
    def poke_level_3_power(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return data.getPower3() if data is not None else 0

    @property
    def poke_level_3_hp(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return data.getHP3() if data is not None else 0

    @property
    def poke_level_4_power(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return data.getPower4() if data is not None else 0

    @property
    def poke_level_4_hp(self) -> int:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return data.getHP4() if data is not None else 0

    @property
    def poke_move_1(self) -> str:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return data.getMove1() if data is not None else ""

    @property
    def poke_move_2(self) -> str:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return data.getMove2() if data is not None else ""

    @property
    def poke_move_3(self) -> str:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return data.getMove3() if data is not None else ""

    @property
    def poke_attribute(self) -> str:
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return data.getAttribute() if data is not None else ""


Familiar.NONE = Familiar()
