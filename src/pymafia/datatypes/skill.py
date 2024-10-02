from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

from pymafia.kolmafia.kolmafia import on_kolmafia_start

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.class_ import Class


@dataclass(frozen=True, order=True)
class Skill:
    NONE: ClassVar[Skill]

    id: int
    name: str

    def __init__(self, key: int | str | None = None):
        if (
            isinstance(key, str) and key.casefold() == self.default_name.casefold()
        ) or key in (
            self.default_id,
            None,
        ):
            object.__setattr__(self, "id", self.default_id)
            object.__setattr__(self, "name", self.default_name)
            return

        id = km.SkillDatabase.getSkillId(key) if isinstance(key, str) else key
        name = km.SkillDatabase.getSkillName(id)
        if name is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "id", id)
        object.__setattr__(self, "name", name)

    def __str__(self) -> str:
        ids = km.SkillDatabase.getSkillIds(self.name, False)
        return f"[{self.id}]{self.name}" if len(ids) > 1 else self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Skill]:
        from pymafia.ash import from_java

        values = km.DataTypes.SKILL_TYPE.allValues()
        return sorted(from_java(values))

    @property
    def default_id(self) -> int:
        return km.DataTypes.SKILL_INIT.contentLong

    @property
    def default_name(self) -> str:
        return km.DataTypes.SKILL_INIT.contentString

    @property
    def type(self) -> str:
        return km.SkillDatabase.getSkillTypeName(self.id)

    @property
    def level(self) -> int:
        return km.SkillDatabase.getSkillLevel(self.id)

    @property
    def image(self) -> str:
        return km.SkillDatabase.getSkillImage(self.id)

    @property
    def traincost(self) -> int:
        return km.SkillDatabase.getSkillPurchaseCost(self.id)

    @property
    def class_(self) -> Class:
        from pymafia.datatypes.class_ import Class

        try:
            return Class(km.SkillDatabase.getSkillCategory(self.id).name)
        except ValueError:
            return Class()

    @property
    def libram(self) -> bool:
        return km.SkillDatabase.isLibramSkill(self.id)

    @property
    def passive(self) -> bool:
        return km.SkillDatabase.isPassive(self.id)

    @property
    def buff(self) -> bool:
        return km.SkillDatabase.isBuff(self.id)

    @property
    def combat(self) -> bool:
        return km.SkillDatabase.isCombat(self.id)

    @property
    def song(self) -> bool:
        return km.SkillDatabase.isSong(self.id)

    @property
    def expression(self) -> bool:
        return km.SkillDatabase.isExpression(self.id)

    @property
    def walk(self) -> bool:
        return km.SkillDatabase.isWalk(self.id)

    @property
    def summon(self) -> bool:
        return km.SkillDatabase.isSummon(self.id)

    @property
    def permable(self) -> bool:
        return km.SkillDatabase.isPermable(self.id)

    @property
    def dailylimit(self) -> int:
        return km.SkillDatabase.getMaxCasts(self.id)

    @property
    def timescast(self) -> int:
        return km.SkillDatabase.getCasts(self.id)


@on_kolmafia_start
def initialize_skill_instances():
    Skill.NONE = Skill()
