from pymafia.kolmafia import km
from pymafia import ash


class Monster:
    def __init__(self, key):
        if key in (None, 0, "none"):
            self.id = 0
            self.name = "none"
            return

        if isinstance(key, str):
            monster_data = km.MonsterDatabase.findMonster(key, True)
        else:
            monster_data = km.MonsterDatabase.findMonsterById(int(key))

        if monster_data is None:
            raise NameError(f"{type(self).__name__} {key!r} not found")

        self.id = monster_data.getId()
        self.name = monster_data.getName()

    @classmethod
    def all(cls):
        values = km.DataTypes.MONSTER_TYPE.allValues()
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
        return self.id != 0

    @property
    def base_hp(self):
        return km.MonsterDatabase.findMonsterById(self.id).getHP()
