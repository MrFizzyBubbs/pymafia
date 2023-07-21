from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, ClassVar

from jpype import JClass

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.effect import Effect
    from pymafia.datatypes.element import Element
    from pymafia.datatypes.phylum import Phylum


Integer = JClass("java.lang.Integer")


@dataclass(frozen=True, order=True)
class Monster:
    NONE: ClassVar[Monster]

    monster: Any = field(default=km.DataTypes.MONSTER_INIT.content, compare=False)
    id: int = km.DataTypes.MONSTER_INIT.contentLong
    name: str = km.DataTypes.MONSTER_INIT.contentString

    def __init__(self, key: int | str | None = None):
        if (isinstance(key, str) and key.casefold() == self.name.casefold()) or key in (
            self.id,
            None,
        ):
            return

        monster = (
            km.MonsterDatabase.findMonster(key, True)
            if isinstance(key, str)
            else km.MonsterDatabase.findMonsterById(key)
        )
        if monster is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "monster", monster)
        object.__setattr__(self, "id", monster.getId())
        object.__setattr__(self, "name", monster.getName())

    def __str__(self) -> str:
        ids = km.MonsterDatabase.getMonsterIds(self.name, False)
        return f"[{self.id}]{self.name}" if len(ids) > 1 else self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Monster]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.MONSTER_TYPE.allValues()
        return sorted(from_java(values))

    @property
    def article(self) -> str:
        return self.monster.getArticle() if self.monster is not None else ""

    @property
    def base_hp(self) -> int:
        return self.monster.getHP() if self.monster is not None else 0

    @property
    def base_attack(self) -> int:
        return self.monster.getAttack() if self.monster is not None else 0

    @property
    def raw_hp(self) -> int:
        return self.monster.getRawHP() if self.monster is not None else 0

    @property
    def raw_attack(self) -> int:
        return self.monster.getRawAttack() if self.monster is not None else 0

    @property
    def raw_defense(self) -> int:
        return self.monster.getRawDefense() if self.monster is not None else 0

    @property
    def base_defense(self) -> int:
        return self.monster.getDefense() if self.monster is not None else 0

    @property
    def base_initiative(self) -> int:
        return self.monster.getInitiative() if self.monster is not None else 0

    @property
    def raw_initiative(self) -> int:
        return self.monster.getRawInitiative() if self.monster is not None else 0

    @property
    def attack_element(self) -> Element:
        from pymafia.datatypes.element import Element

        return (
            Element(self.monster.getAttackElement().toString())
            if self.monster is not None
            else Element()
        )

    @property
    def attack_elements(self) -> list[Element]:
        from pymafia.datatypes.element import Element

        if self.monster is None:
            return []
        return [Element(x.toString()) for x in self.monster.getAttackElements()]

    @property
    def defense_element(self) -> Element:
        from pymafia.datatypes.element import Element

        return (
            Element(self.monster.getDefenseElement().toString())
            if self.monster is not None
            else Element()
        )

    @property
    def physical_resistance(self) -> int:
        return self.monster.getPhysicalResistance() if self.monster is not None else 0

    @property
    def elemental_resistance(self) -> int:
        return self.monster.getElementalResistance() if self.monster is not None else 0

    @property
    def min_meat(self) -> int:
        return self.monster.getMinMeat() if self.monster is not None else 0

    @property
    def max_meat(self) -> int:
        return self.monster.getMaxMeat() if self.monster is not None else 0

    @property
    def min_sprinkles(self) -> int:
        return self.monster.getMinSprinkles() if self.monster is not None else 0

    @property
    def max_sprinkles(self) -> int:
        return self.monster.getMaxSprinkles() if self.monster is not None else 0

    @property
    def base_mainstat_exp(self) -> float:
        return self.monster.getExperience() if self.monster is not None else 0

    @property
    def group(self) -> int:
        return self.monster.getGroup() if self.monster is not None else 0

    @property
    def phylum(self) -> Phylum:
        from pymafia.datatypes.phylum import Phylum

        return (
            Phylum(self.monster.getPhylum().toString())
            if self.monster is not None
            else Phylum()
        )

    @property
    def poison(self) -> Effect:
        from pymafia.datatypes.effect import Effect

        if self.monster is None:
            return Effect()
        poison_level = self.monster.getPoison()
        if poison_level == Integer.MAX_VALUE:
            return Effect()
        poison_name = km.EffectDatabase.getEffectName(
            km.EffectDatabase.POISON_ID[poison_level]
        )
        return Effect(poison_name)

    @property
    def boss(self) -> bool:
        return self.monster.isBoss() if self.monster is not None else False

    @property
    def copyable(self) -> bool:
        return self.monster.isNoCopy() if self.monster is not None else False

    @property
    def image(self) -> str:
        return self.monster.getImage() if self.monster is not None else ""

    @property
    def images(self) -> list[str]:
        return list(self.monster.getImages()) if self.monster is not None else []

    @property
    def random_modifiers(self) -> list[str]:
        return (
            list(self.monster.getRandomModifiers()) if self.monster is not None else []
        )

    @property
    def sub_types(self) -> list[str]:
        return list(self.monster.getSubTypes()) if self.monster is not None else []

    @property
    def manuel_name(self) -> str:
        return self.monster.getManuelName() if self.monster is not None else ""

    @property
    def wiki_name(self) -> str:
        return self.monster.getWikiName() if self.monster is not None else ""

    @property
    def attributes(self) -> str:
        return self.monster.getAttributes() if self.monster is not None else ""


Monster.NONE = Monster()
