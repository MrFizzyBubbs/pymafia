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
    Modifier,
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
Matcher = JClass("java.util.regex.Matcher")

TYPESPEC_CONVERSIONS = {
    km.DataTypes.TypeSpec.BOOLEAN: bool,
    km.DataTypes.TypeSpec.INT: int,
    km.DataTypes.TypeSpec.FLOAT: float,
    km.DataTypes.TypeSpec.STRING: str,
    km.DataTypes.TypeSpec.STRICT_STRING: str,
    km.DataTypes.TypeSpec.BUFFER: str,
    km.DataTypes.TypeSpec.ITEM: Item,
    km.DataTypes.TypeSpec.LOCATION: Location,
    km.DataTypes.TypeSpec.CLASS: Class,
    km.DataTypes.TypeSpec.STAT: Stat,
    km.DataTypes.TypeSpec.SKILL: Skill,
    km.DataTypes.TypeSpec.EFFECT: Effect,
    km.DataTypes.TypeSpec.FAMILIAR: Familiar,
    km.DataTypes.TypeSpec.SLOT: Slot,
    km.DataTypes.TypeSpec.MONSTER: Monster,
    km.DataTypes.TypeSpec.ELEMENT: Element,
    km.DataTypes.TypeSpec.COINMASTER: Coinmaster,
    km.DataTypes.TypeSpec.PHYLUM: Phylum,
    km.DataTypes.TypeSpec.BOUNTY: Bounty,
    km.DataTypes.TypeSpec.THRALL: Thrall,
    km.DataTypes.TypeSpec.SERVANT: Servant,
    km.DataTypes.TypeSpec.VYKEA: Vykea,
    km.DataTypes.TypeSpec.PATH: Path,
    km.DataTypes.TypeSpec.MODIFIER: Modifier,
}


def to_java(obj: Any) -> Any:
    """Convert to a Java KoLmafia Value."""
    if isinstance(obj, (bool, int, float, str)):
        return km.Value(obj)
    if isinstance(obj, MAFIA_DATATYPES):
        parser = getattr(km.DataTypes, f"parse{type(obj).__name__}Value")
        return parser(str(obj), False)
    if isinstance(obj, Matcher):
        return km.Value(km.DataTypes.MATCHER_TYPE, obj.pattern(), obj)
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
    raise TypeError(f"unsupported type {type(obj).__name__!r}")


def from_java(obj: Any) -> Any:
    """Convert from a Java KoLmafia Value."""
    jtype = obj.getType()
    jtypespec = jtype.getType()

    if jtypespec == km.DataTypes.TypeSpec.VOID:
        return None
    if jtypespec in TYPESPEC_CONVERSIONS:
        return TYPESPEC_CONVERSIONS[jtypespec](obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.MATCHER:
        return obj.rawValue()
    if jtypespec == km.DataTypes.TypeSpec.AGGREGATE:
        if isinstance(obj.content, abc.Mapping):
            return {from_java(k): from_java(v) for k, v in obj.content.items()}
        if isinstance(obj.content, abc.Iterable):
            return [from_java(x) for x in obj.content]
    if jtypespec == km.DataTypes.TypeSpec.RECORD:
        return {from_java(k): from_java(v) for k, v in zip(obj.keys(), obj.content)}
    raise TypeError(
        f"unsupported type {jtype.getName()!r} (TypeSpec.{jtypespec.toString()})"
    )
