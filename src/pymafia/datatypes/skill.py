import pymafia.kolmafia as km
from pymafia import ash, datatypes


class Skill:
    id = -1
    name = "none"

    def __init__(self, key=None):
        if key in (None, self.id, self.name):
            return

        id_ = km.SkillDatabase.getSkillId(key) if isinstance(key, str) else key
        name = km.SkillDatabase.getSkillName(id_)

        if name is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = id_
        self.name = name

    def __str__(self):
        ids = km.SkillDatabase.getSkillIds(self.name, False)
        return f"[{self.id}]{self.name}" if len(ids) > 1 else self.name

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
        values = km.DataTypes.SKILL_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def type_(self):
        return km.SkillDatabase.getSkillTypeName(self.id)

    @property
    def level(self):
        return km.SkillDatabase.getSkillLevel(self.id)

    @property
    def image(self):
        return km.SkillDatabase.getSkillImage(self.id)

    @property
    def traincost(self):
        return km.SkillDatabase.getSkillPurchaseCost(self.id)

    @property
    def class_(self):
        return datatypes.Class(km.SkillDatabase.getSkillCategory(self.id) or None)

    @property
    def libram(self):
        return km.SkillDatabase.isLibramSkill(self.id)

    @property
    def passive(self):
        return km.SkillDatabase.isPassive(self.id)

    @property
    def buff(self):
        return km.SkillDatabase.isBuff(self.id)

    @property
    def combat(self):
        return km.SkillDatabase.isCombat(self.id)

    @property
    def song(self):
        return km.SkillDatabase.isSong(self.id)

    @property
    def expression(self):
        return km.SkillDatabase.isExpression(self.id)

    @property
    def walk(self):
        return km.SkillDatabase.isWalk(self.id)

    @property
    def summon(self):
        return km.SkillDatabase.isSummon(self.id)

    @property
    def permable(self):
        return km.SkillDatabase.isPermable(self.id)

    @property
    def dailylimit(self):
        return km.SkillDatabase.getMaxCasts(self.id)

    @property
    def timescast(self):
        return km.SkillDatabase.getCasts(self.id)
