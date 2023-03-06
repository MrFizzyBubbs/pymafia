import collections

from pymafia import datatypes
from pymafia.kolmafia import km

TypeSpec = getattr(km, "textui.DataTypes$TypeSpec")
TypeSpec.__hash__ = TypeSpec.hashCode  # Monkey-patch to make hashable

TYPE_CONVERSIONS = {
    TypeSpec.BOOLEAN: bool,
    TypeSpec.INT: int,
    TypeSpec.FLOAT: float,
    TypeSpec.STRING: str,
    TypeSpec.BUFFER: str,
    TypeSpec.ITEM: datatypes.Item,
    TypeSpec.LOCATION: datatypes.Location,
    TypeSpec.CLASS: datatypes.Class,
    TypeSpec.STAT: datatypes.Stat,
    TypeSpec.SKILL: datatypes.Skill,
    TypeSpec.EFFECT: datatypes.Effect,
    TypeSpec.FAMILIAR: datatypes.Familiar,
    TypeSpec.SLOT: datatypes.Slot,
    TypeSpec.MONSTER: datatypes.Monster,
    TypeSpec.ELEMENT: datatypes.Element,
    TypeSpec.COINMASTER: datatypes.Coinmaster,
    TypeSpec.PHYLUM: datatypes.Phylum,
    TypeSpec.BOUNTY: datatypes.Bounty,
    TypeSpec.THRALL: datatypes.Thrall,
    TypeSpec.SERVANT: datatypes.Servant,
    TypeSpec.VYKEA: datatypes.Vykea,
    TypeSpec.PATH: datatypes.Path,
}

TreeMap = km.autoclass("java.util.TreeMap")
ArrayList = km.autoclass("java.util.ArrayList")
String = km.autoclass("java.lang.String")
ByteArrayInputStream = km.autoclass("java.io.ByteArrayInputStream")


def __getattr__(name):
    return AshFunction(name)


def to_java(obj):
    if obj is None or isinstance(obj, (int, float, str)):
        return km.Value(obj)

    if isinstance(obj, tuple(datatypes.MAFIA_TYPES)):
        parser = getattr(km.DataTypes, f"parse{type(obj).__name__}Value")
        return parser(str(obj), False)

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

    if jtype in [TypeSpec.VOID, TypeSpec.ANY]:
        return None
    if jtype in TYPE_CONVERSIONS:
        return TYPE_CONVERSIONS[jtype](obj.toJSON())
    if jtype == TypeSpec.AGGREGATE and isinstance(obj.content, TreeMap):
        return {to_python(x.key): to_python(x.value) for x in obj.content.entrySet()}
    if jtype == TypeSpec.AGGREGATE and isinstance(obj.content, list):
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
