from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from .effect import Effect
    from .element import Element
    from .phylum import Phylum


Integer = km.autoclass("java.lang.Integer")


@total_ordering
class Monster:
    id: int = 0
    name: str = "none"
    monster: Any = None

    def __init__(self, key: int | str | None = None):
        if key in (None, self.name, self.id):
            return

        monster = (
            km.MonsterDatabase.findMonster(key, True)
            if isinstance(key, str)
            else km.MonsterDatabase.findMonsterById(key)
        )
        if monster is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = monster.getId()
        self.name = monster.getName()
        self.monster = monster

    def __str__(self) -> str:
        ids = km.MonsterDatabase.getMonsterIds(self.name, False)
        return f"[{self.id}]{self.name}" if len(ids) > 1 else self.name

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
    def all(cls) -> list[Monster]:
        from pymafia import ash

        values = km.DataTypes.MONSTER_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def article(self) -> str:
        return self.monster.getArticle() if self else ""

    @property
    def base_hp(self) -> int:
        return self.monster.getHP() if self else 0

    @property
    def base_attack(self) -> int:
        return self.monster.getAttack() if self else 0

    @property
    def raw_hp(self) -> int:
        return self.monster.getRawHP() if self else 0

    @property
    def raw_attack(self) -> int:
        return self.monster.getRawAttack() if self else 0

    @property
    def raw_defense(self) -> int:
        return self.monster.getRawDefense() if self else 0

    @property
    def base_defense(self) -> int:
        return self.monster.getDefense() if self else 0

    @property
    def base_initiative(self) -> int:
        return self.monster.getInitiative() if self else 0

    @property
    def raw_initiative(self) -> int:
        return self.monster.getRawInitiative() if self else 0

    @property
    def attack_element(self) -> Element:
        from .element import Element

        return (
            Element(self.monster.getAttackElement().toString())
            if self
            else Element.NONE
        )

    @property
    def attack_elements(self) -> list[Element]:
        if not self:
            return []
        return [Element(x.toString()) for x in self.monster.getAttackElements()]

    @property
    def defense_element(self) -> Element:
        from .element import Element

        return (
            Element(self.monster.getDefenseElement().toString())
            if self
            else Element.NONE
        )

    @property
    def physical_resistance(self) -> int:
        return self.monster.getPhysicalResistance() if self else 0

    @property
    def elemental_resistance(self) -> int:
        return self.monster.getElementalResistance() if self else 0

    @property
    def min_meat(self) -> int:
        return self.monster.getMinMeat() if self else 0

    @property
    def max_meat(self) -> int:
        return self.monster.getMaxMeat() if self else 0

    @property
    def min_sprinkles(self) -> int:
        return self.monster.getMinSprinkles() if self else 0

    @property
    def max_sprinkles(self) -> int:
        return self.monster.getMaxSprinkles() if self else 0

    @property
    def base_mainstat_exp(self) -> float:
        return self.monster.getExperience() if self else 0

    @property
    def group(self) -> int:
        return self.monster.getGroup() if self else 0

    @property
    def phylum(self) -> Phylum:
        from .phylum import Phylum

        return Phylum(self.monster.getPhylum().toString()) if self else Phylum.NONE

    @property
    def poison(self) -> Effect:
        from .effect import Effect

        if not self:
            return Effect(None)
        poison_level = self.monster.getPoison()
        if poison_level == Integer.MAX_VALUE:
            return Effect(None)
        poison_name = km.EffectDatabase.getEffectName(
            km.EffectDatabase.POISON_ID[poison_level]
        )
        return Effect(poison_name)

    @property
    def boss(self) -> bool:
        return self.monster.isBoss() if self else False

    @property
    def copyable(self) -> bool:
        return self.monster.isNoCopy() if self else False

    @property
    def image(self) -> str:
        return self.monster.getImage() if self else ""

    @property
    def images(self) -> list[str]:
        return list(self.monster.getImages()) if self else []

    @property
    def random_modifiers(self) -> list[str]:
        return list(self.monster.getRandomModifiers()) if self else []

    @property
    def sub_types(self) -> list[str]:
        return list(self.monster.getSubTypes()) if self else []

    @property
    def manuel_name(self) -> str:
        return self.monster.getManuelName() if self else ""

    @property
    def wiki_name(self) -> str:
        return self.monster.getWikiName() if self else ""

    @property
    def attributes(self) -> str:
        return self.monster.getAttributes() if self else ""
