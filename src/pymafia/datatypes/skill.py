from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING, Any

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from .class_ import Class


@total_ordering
class Skill:
    id: int = -1
    name: str = "none"

    def __init__(self, key: int | str | None = None):
        if key in (None, self.name, self.id):
            return

        id = km.SkillDatabase.getSkillId(key) if isinstance(key, str) else key
        name = km.SkillDatabase.getSkillName(id)
        if name is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = id
        self.name = name

    def __str__(self) -> str:
        ids = km.SkillDatabase.getSkillIds(self.name, False)
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
    def all(cls) -> list[Skill]:
        from pymafia import ash

        values = km.DataTypes.SKILL_TYPE.allValues()
        return sorted(ash.to_python(values))

    @property
    def type_(self) -> str:
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
        from .class_ import Class

        return Class(km.SkillDatabase.getSkillCategory(self.id) or None)

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
