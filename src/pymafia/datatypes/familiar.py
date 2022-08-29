import pymafia.kolmafia as km
from pymafia import ash, datatypes


class Familiar:
    id = -1
    name = "none"

    def __init__(self, key=None):
        if key in (None, self.id, self.name):
            return

        id_ = km.FamiliarDatabase.getFamiliarId(key) if isinstance(key, str) else key
        name = km.FamiliarDatabase.getFamiliarName(id_)

        if name is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = id_
        self.name = name

    def __str__(self):
        return self.name

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
        values = km.DataTypes.FAMILIAR_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def hatchling(self):
        hatchling_id = km.FamiliarDatabase.getFamiliarLarva(self.id)
        return datatypes.Item(hatchling_id) or None

    @property
    def image(self):
        return km.FamiliarDatabase.getFamiliarImageLocation(self.id)

    @property
    def nickname(self):
        fam = km.KoLCharacter.findFamiliar(self.id)
        return fam.getName()

    @property
    def experience(self):
        fam = km.KoLCharacter.findFamiliar(self.id)
        return fam.getTotalExperience()

    @property
    def charges(self):
        fam = km.KoLCharacter.findFamiliar(self.id)
        return fam.getCharges()

    @property
    def drop_name(self):
        return km.FamiliarData.dropName(self.id) or ""

    @property
    def drop_item(self):
        item = km.FamiliarData.dropItem(self.id)
        return None if item is None else datatypes.Item(item.getItemId())

    @property
    def drops_today(self):
        return km.FamiliarData.dropsToday(self.id)

    @property
    def drops_limit(self):
        return km.FamiliarData.dropsToday(self.id)

    @property
    def fights_today(self):
        return km.FamiliarData.fightsToday(self.id)

    @property
    def fights_limit(self):
        return km.FamiliarData.fightDailyCap(self.id)

    @property
    def combat(self):
        return km.FamiliarDatabase.isCombatType(self.id)

    @property
    def physical_damage(self):
        return km.FamiliarDatabase.isCombat0Type(self.id)

    @property
    def elemental_damage(self):
        return km.FamiliarDatabase.isCombat1Type(self.id)

    @property
    def block(self):
        return km.FamiliarDatabase.isBlockType(self.id)

    @property
    def delevel(self):
        return km.FamiliarDatabase.isDelevelType(self.id)

    @property
    def hp_during_combat(self):
        return km.FamiliarDatabase.isHp0Type(self.id)

    @property
    def mp_during_combat(self):
        return km.FamiliarDatabase.isMp0Type(self.id)

    @property
    def other_action_during_combat(self):
        return km.FamiliarDatabase.isOther0Type(self.id)

    @property
    def hp_after_combat(self):
        return km.FamiliarDatabase.isHp1Type(self.id)

    @property
    def mp_after_combat(self):
        return km.FamiliarDatabase.isMp1Type(self.id)

    @property
    def other_action_after_combat(self):
        return km.FamiliarDatabase.isOther1Type(self.id)

    @property
    def passive(self):
        return km.FamiliarDatabase.isPassiveType(self.id)

    @property
    def underwater(self):
        return km.FamiliarDatabase.isUnderwaterType(self.id)

    @property
    def variable(self):
        return km.FamiliarDatabase.isVariableType(self.id)

    @property
    def attributes(self):
        attrs = km.FamiliarDatabase.getFamiliarAttributes(self.id)
        return [] if attrs is None else list(attrs)

    @property
    def poke_level(self):
        fam = km.KoLCharacter.findFamiliar(self.id)
        return 0 if fam is None else fam.getPokeLevel()

    @property
    def poke_level_2_power(self):
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getPower2()

    @property
    def poke_level_2_hp(self):
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getHP2()

    @property
    def poke_level_3_power(self):
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getPower3()

    @property
    def poke_level_3_hp(self):
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getHP3()

    @property
    def poke_level_4_power(self):
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getPower4()

    @property
    def poke_level_4_hp(self):
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return 0 if data is None else data.getHP4()

    @property
    def poke_move_1(self):
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return "" if data is None else data.getMove1()

    @property
    def poke_move_2(self):
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return "" if data is None else data.getMove2()

    @property
    def poke_move_3(self):
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return "" if data is None else data.getMove3()

    @property
    def poke_attribute(self):
        data = km.FamiliarDatabase.getPokeDataById(self.id)
        return "" if data is None else data.getAttribute()
