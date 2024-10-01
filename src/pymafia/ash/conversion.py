from collections import abc
from typing import Any

from jpype import JClass

from pymafia.datatypes import (
    SPECIAL_DATATYPES,
    Bounty,
    Class,
    Coinmaster,
    Effect,
    Element,
    Familiar,
    Item,
    Location,
    Matcher,
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


def to_java(obj: Any) -> Any:
    """Convert to a Java KoLmafia Value."""
    if isinstance(obj, (bool, int, float, str)):
        return km.Value(obj)
    if isinstance(obj, SPECIAL_DATATYPES):
        parser = getattr(km.DataTypes, f"parse{type(obj).__name__}Value")
        return parser(str(obj), False)
    if isinstance(obj, Matcher):
        return km.Value(
            km.DataTypes.MATCHER_TYPE, obj.pattern().toString(), obj.__wrapped__
        )
    if isinstance(obj, abc.Mapping):
        JTreeMap = JClass("java.util.TreeMap")

        jmap = JTreeMap()
        for k, v in obj.items():
            jk = to_java(k)
            jv = to_java(v)
            jmap.put(jk, jv)
        data_type = jmap.firstEntry().getValue().getType()
        index_type = jmap.firstEntry().getKey().getType()
        aggregate_type = km.AggregateType(data_type, index_type)
        return km.MapValue(aggregate_type, jmap)
    if isinstance(obj, abc.Iterable):
        JArrayList = JClass("java.util.ArrayList")

        jlist = JArrayList()
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

    # Primitive types
    if jtypespec == km.DataTypes.TypeSpec.VOID:
        return None
    if jtypespec == km.DataTypes.TypeSpec.BOOLEAN:
        return bool(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.INT:
        return int(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.FLOAT:
        return float(obj.toJSON())
    if jtypespec in (
        km.DataTypes.TypeSpec.STRING,
        km.DataTypes.TypeSpec.STRICT_STRING,
        km.DataTypes.TypeSpec.BUFFER,
    ):
        return str(obj.toJSON())

    # Special types
    if jtypespec == km.DataTypes.TypeSpec.ITEM:
        return Item(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.LOCATION:
        return Location(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.CLASS:
        return Class(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.STAT:
        return Stat(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.SKILL:
        return Skill(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.EFFECT:
        return Effect(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.FAMILIAR:
        return Familiar(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.SLOT:
        return Slot(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.MONSTER:
        return Monster(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.ELEMENT:
        return Element(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.COINMASTER:
        return Coinmaster(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.PHYLUM:
        return Phylum(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.BOUNTY:
        return Bounty(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.THRALL:
        return Thrall(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.SERVANT:
        return Servant(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.VYKEA:
        return Vykea(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.PATH:
        return Path(obj.toJSON())
    if jtypespec == km.DataTypes.TypeSpec.MODIFIER:
        return Modifier(obj.toJSON())

    if jtypespec == km.DataTypes.TypeSpec.MATCHER:
        return Matcher(obj.rawValue())

    # Composite types
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
