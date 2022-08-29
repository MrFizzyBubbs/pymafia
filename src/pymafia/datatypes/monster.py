import pymafia.kolmafia as km
from pymafia import ash, datatypes

Integer = km.autoclass("java.lang.Integer")


class Monster:
    id = 0
    name = "none"
    monster = None

    def __init__(self, key=None):
        if key in (None, self.id, self.name):
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

    def __str__(self):
        ids = km.MonsterDatabase.getMonsterIds(self.name, False)
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
        values = km.DataTypes.MONSTER_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def base_hp(self):
        return self.monster.getHP() if self else 0

    @property
    def base_attack(self):
        return self.monster.getAttack() if self else 0

    @property
    def raw_hp(self):
        return self.monster.getRawHP() if self else 0

    @property
    def raw_attack(self):
        return self.monster.getRawAttack() if self else 0

    @property
    def raw_defense(self):
        return self.monster.getRawDefense() if self else 0

    @property
    def base_defense(self):
        return self.monster.getDefense() if self else 0

    @property
    def base_initiative(self):
        return self.monster.getInitiative() if self else 0

    @property
    def raw_initiative(self):
        return self.monster.getRawInitiative() if self else 0

    @property
    def attack_element(self):
        return (
            datatypes.Element(self.monster.getAttackElement().toString())
            if self
            else datatypes.Element.NONE
        )

    @property
    def defense_element(self):
        return (
            datatypes.Element(self.monster.getDefenseElement().toString())
            if self
            else datatypes.Element.NONE
        )

    @property
    def physical_resistance(self):
        return self.monster.getPhysicalResistance() if self else 0

    @property
    def min_meat(self):
        return self.monster.getMinMeat() if self else 0

    @property
    def max_meat(self):
        return self.monster.getMaxMeat() if self else 0

    @property
    def min_sprinkles(self):
        return self.monster.getMinSprinkles() if self else 0

    @property
    def max_sprinkles(self):
        return self.monster.getMaxSprinkles() if self else 0

    @property
    def base_mainstat_exp(self):
        return self.monster.getExperience() if self else 0

    @property
    def phylum(self):
        return (
            datatypes.Phylum(self.monster.getPhylum().toString())
            if self
            else datatypes.Phylum.NONE
        )

    @property
    def poison(self):
        if not self:
            return None
        poison_level = self.monster.getPoison()
        if poison_level == Integer.MAX_VALUE:
            return None
        poison_name = km.EffectDatabase.getEffectName(
            km.EffectDatabase.POISON_ID[poison_level]
        )
        return datatypes.Effect(poison_name)

    @property
    def boss(self):
        return self.monster.isBoss() if self else False

    @property
    def copyable(self):
        return self.monster.isNoCopy() if self else False

    @property
    def image(self):
        return self.monster.getImage() if self else ""

    @property
    def images(self):
        return list(self.monster.getImages()) if self else []

    @property
    def random_modifiers(self):
        return list(self.monster.getRandomModifiers()) if self else []

    @property
    def sub_types(self):
        return list(self.monster.getSubTypes()) if self else []

    @property
    def manuel_name(self):
        return self.monster.getManuelName() if self else ""

    @property
    def wiki_name(self):
        return self.monster.getWikiName() if self else ""

    @property
    def attributes(self):
        return self.monster.getAttributes() if self else ""
