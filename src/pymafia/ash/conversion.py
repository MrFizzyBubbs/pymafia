from collections import abc
from typing import Any

from jpype import JClass

from pymafia.datatypes import (
    MAFIA_DATATYPES,
    Bounty,
    Class,
    Coinmaster,
    Effect,
    Element,
    Familiar,
    Item,
    Location,
    Monster,
    Path,
    Phylum,
    Servant,
    Skill,
    Slot,
    Stat,
    Thrall,
    Vykea,
)
from pymafia.kolmafia import km

TreeMap = JClass("java.util.TreeMap")
ArrayList = JClass("java.util.ArrayList")

TYPE_CONVERSIONS = {
    km.DataTypes.BOOLEAN_TYPE: bool,
    km.DataTypes.INT_TYPE: int,
    km.DataTypes.FLOAT_TYPE: float,
    km.DataTypes.STRING_TYPE: str,
    km.DataTypes.BUFFER_TYPE: str,
    km.DataTypes.ITEM_TYPE: Item,
    km.DataTypes.LOCATION_TYPE: Location,
    km.DataTypes.CLASS_TYPE: Class,
    km.DataTypes.STAT_TYPE: Stat,
    km.DataTypes.SKILL_TYPE: Skill,
    km.DataTypes.EFFECT_TYPE: Effect,
    km.DataTypes.FAMILIAR_TYPE: Familiar,
    km.DataTypes.SLOT_TYPE: Slot,
    km.DataTypes.MONSTER_TYPE: Monster,
    km.DataTypes.ELEMENT_TYPE: Element,
    km.DataTypes.COINMASTER_TYPE: Coinmaster,
    km.DataTypes.PHYLUM_TYPE: Phylum,
    km.DataTypes.BOUNTY_TYPE: Bounty,
    km.DataTypes.THRALL_TYPE: Thrall,
    km.DataTypes.SERVANT_TYPE: Servant,
    km.DataTypes.VYKEA_TYPE: Vykea,
    km.DataTypes.PATH_TYPE: Path,
}


def to_java(obj: Any) -> Any:
    """Convert a Python object to a KoLmafia Value or PluralValue."""
    if isinstance(obj, (bool, int, float, str)):
        return km.Value(obj)

    if isinstance(obj, MAFIA_DATATYPES):
        parser = getattr(km.DataTypes, f"parse{type(obj).__name__}Value")
        return parser(str(obj), False)

    if isinstance(obj, abc.Mapping):
        jmap = TreeMap()
        for k, v in obj.items():
            jk = to_java(k)
            jv = to_java(v)
            jmap.put(jk, jv)
        data_type = jmap.firstEntry().getValue().getType()
        index_type = jmap.firstEntry().getKey().getType()
        aggregate_type = km.AggregateType(data_type, index_type)
        return km.MapValue(aggregate_type, jmap)

    if isinstance(obj, abc.Iterable):
        jlist = ArrayList()
        for item in obj:
            jitem = to_java(item)
            jlist.add(jitem)
        data_type = jlist.get(0).getType()
        size = jlist.size()
        aggregate_type = km.AggregateType(data_type, size)
        return km.ArrayValue(aggregate_type, jlist)

    raise TypeError(f"unsupported type: {type(obj).__name__!r}")


def from_java(obj: Any) -> Any:
    """Convert a KoLmafia Value or PluralValue to a Python object."""
    jtype = obj.getType()

    if jtype == km.DataTypes.VOID_TYPE:
        return None

    if jtype in TYPE_CONVERSIONS:
        return TYPE_CONVERSIONS[jtype](obj.toJSON())

    if isinstance(jtype, km.AggregateType) and isinstance(obj.content, abc.Mapping):
        return {from_java(k): from_java(v) for k, v in obj.content.items()}

    if isinstance(jtype, km.AggregateType) and isinstance(obj.content, abc.Iterable):
        return [from_java(x) for x in obj.content]

    raise TypeError(f"unsupported type: {jtype.getName()!r}")
