import collections

from pymafia.datatypes import (
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

SIMPLE_TYPES = {
    km.DataTypes.TYPE_BOOLEAN: bool,
    km.DataTypes.TYPE_INT: int,
    km.DataTypes.TYPE_FLOAT: float,
    km.DataTypes.TYPE_STRING: str,
    km.DataTypes.TYPE_BUFFER: str,
    km.DataTypes.TYPE_ITEM: Item,
    km.DataTypes.TYPE_LOCATION: Location,
    km.DataTypes.TYPE_CLASS: Class,
    km.DataTypes.TYPE_STAT: Stat,
    km.DataTypes.TYPE_SKILL: Skill,
    km.DataTypes.TYPE_EFFECT: Effect,
    km.DataTypes.TYPE_FAMILIAR: Familiar,
    km.DataTypes.TYPE_SLOT: Slot,
    km.DataTypes.TYPE_MONSTER: Monster,
    km.DataTypes.TYPE_ELEMENT: Element,
    km.DataTypes.TYPE_COINMASTER: Coinmaster,
    km.DataTypes.TYPE_PHYLUM: Phylum,
    km.DataTypes.TYPE_BOUNTY: Bounty,
    km.DataTypes.TYPE_THRALL: Thrall,
    km.DataTypes.TYPE_SERVANT: Servant,
    km.DataTypes.TYPE_VYKEA: Vykea,
    km.DataTypes.TYPE_PATH: Path,
}

TreeMap = km.autoclass("java.util.TreeMap")
ArrayList = km.autoclass("java.util.ArrayList")
String = km.autoclass("java.lang.String")
ByteArrayInputStream = km.autoclass("java.io.ByteArrayInputStream")


def __getattr__(name):
    return AshFunction(name)


def to_java(obj):
    if isinstance(obj, (type(None), int, float, str)):
        return km.Value(obj)

    if isinstance(obj, tuple(SIMPLE_TYPES.values())):
        parse_value = getattr(km.DataTypes, f"parse{type(obj).__name__}Value")
        return parse_value(str(obj), False)

    if isinstance(obj, collections.abc.Mapping):
        jmap = TreeMap()
        for k, v in obj.items():
            jk = to_java(k)
            jv = to_java(v)
            jmap.put(jk, jv)
        data_type = jmap.getFirstEntry().getValue().getType()
        index_type = jmap.getFirstEntry().getKey().getType()
        aggregate_type = km.AggregateType(data_type, index_type)
        return km.MapValue(aggregate_type, jmap)

    if isinstance(obj, collections.abc.Iterable):
        jlist = ArrayList()
        for item in obj:
            jitem = to_java(item)
            jlist.add(jitem)
        data_type = jlist.get(0).getType()
        size = jlist.size()
        aggregate_type = km.AggregateType(data_type, size)
        return km.ArrayValue(aggregate_type, jlist)

    raise TypeError(f"unsupported type: {type(obj).__name__!r}")


def to_python(obj):
    jtype = obj.getType().getType()
    jname = obj.getType().getName()

    if jtype in [km.DataTypes.TYPE_VOID, km.DataTypes.TYPE_ANY]:
        return None
    if jtype in SIMPLE_TYPES:
        return SIMPLE_TYPES[jtype](obj.toJSON())
    if jtype == km.DataTypes.TYPE_AGGREGATE and isinstance(obj.content, TreeMap):
        return {to_python(x.key): to_python(x.value) for x in obj.content.entrySet()}
    if jtype == km.DataTypes.TYPE_AGGREGATE and isinstance(obj.content, list):
        return [to_python(x) for x in obj.content]

    raise TypeError(f"unsupported type: {jtype!r} ({jname!r})")


def ashref(command=""):
    names = set()
    for func in km.RuntimeLibrary.getFunctions():
        name = func.getName()
        if command.lower() in name:
            names.add(name)
    return sorted(names)


def script(lines, raw=False):
    stream = ByteArrayInputStream(String(lines).getBytes())
    interpreter = km.AshRuntime()
    interpreter.validate(None, stream)
    value = interpreter.execute("main", None)
    return value if raw else to_python(value)


class AshFunction:
    def __init__(self, name):
        self.name = name
        self.func = getattr(km.RuntimeLibrary, self.name)

    def __call__(self, *args, raw=False):
        interpreter = km.AshRuntime()
        jargs = [to_java(arg) for arg in args]
        value = self.func(interpreter, *jargs)
        return value if raw else to_python(value)

    @property
    def signatures(self):
        functions = km.RuntimeLibrary.getFunctions().findFunctions(self.name)
        return [f"{f.getType().toString()} {f.getSignature()}" for f in functions]

    @property
    def wiki(self):
        return f"https://wiki.kolmafia.us/index.php/{self.name}"
