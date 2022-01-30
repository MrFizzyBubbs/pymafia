from pymafia.kolmafia import km
from pymafia import ash


class Skill:
    def __init__(self, key):
        if key in (None, -1, "none"):
            self.id = -1
            self.name = "none"
            return

        id_ = int(km.SkillDatabase.getSkillId(key) if isinstance(key, str) else key)
        name = km.SkillDatabase.getSkillName(id_)

        if name is None:
            raise NameError(f"{type(self).__name__} {key!r} not found")

        self.id = id_
        self.name = name

    @classmethod
    def all(cls):
        values = km.DataTypes.SKILL_TYPE.allValues()
        return sorted(ash.from_java(values), key=lambda x: x.id)

    def __hash__(self):
        return hash((self.id, self.name))

    def __str__(self):
        return f"[{self.id}]{self.name}" if self else self.name

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __eq__(self, other):
        return isinstance(other, type(self)) and (self.id, self.name) == (
            other.id,
            other.name,
        )

    def __bool__(self):
        return self.id != -1
