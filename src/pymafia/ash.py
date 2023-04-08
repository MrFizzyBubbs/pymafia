import collections

from jpype import JClass

from pymafia import datatypes
from pymafia.kolmafia import km

TreeMap = JClass("java.util.TreeMap")
ArrayList = JClass("java.util.ArrayList")
String = JClass("java.lang.String")
ByteArrayInputStream = JClass("java.io.ByteArrayInputStream")

TYPE_CONVERSIONS = {
    km.DataTypes.TypeSpec.BOOLEAN: bool,
    km.DataTypes.TypeSpec.INT: int,
    km.DataTypes.TypeSpec.FLOAT: float,
    km.DataTypes.TypeSpec.STRING: str,
    km.DataTypes.TypeSpec.BUFFER: str,
    km.DataTypes.TypeSpec.ITEM: datatypes.Item,
    km.DataTypes.TypeSpec.LOCATION: datatypes.Location,
    km.DataTypes.TypeSpec.CLASS: datatypes.Class,
    km.DataTypes.TypeSpec.STAT: datatypes.Stat,
    km.DataTypes.TypeSpec.SKILL: datatypes.Skill,
    km.DataTypes.TypeSpec.EFFECT: datatypes.Effect,
    km.DataTypes.TypeSpec.FAMILIAR: datatypes.Familiar,
    km.DataTypes.TypeSpec.SLOT: datatypes.Slot,
    km.DataTypes.TypeSpec.MONSTER: datatypes.Monster,
    km.DataTypes.TypeSpec.ELEMENT: datatypes.Element,
    km.DataTypes.TypeSpec.COINMASTER: datatypes.Coinmaster,
    km.DataTypes.TypeSpec.PHYLUM: datatypes.Phylum,
    km.DataTypes.TypeSpec.BOUNTY: datatypes.Bounty,
    km.DataTypes.TypeSpec.THRALL: datatypes.Thrall,
    km.DataTypes.TypeSpec.SERVANT: datatypes.Servant,
    km.DataTypes.TypeSpec.VYKEA: datatypes.Vykea,
    km.DataTypes.TypeSpec.PATH: datatypes.Path,
}


def __getattr__(name):
    return AshFunction(name)


def to_java(obj):
    if obj is None or isinstance(obj, (int, float, str)):
        return km.Value(obj)

    if isinstance(obj, tuple(datatypes.MAFIA_DATATYPES)):
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

    if jtype in [km.DataTypes.TypeSpec.VOID, km.DataTypes.TypeSpec.ANY]:
        return None
    if jtype in TYPE_CONVERSIONS:
        return TYPE_CONVERSIONS[jtype](obj.toJSON())
    if jtype == km.DataTypes.TypeSpec.AGGREGATE and isinstance(obj.content, TreeMap):
        return {
            to_python(x.getKey()): to_python(x.getValue())
            for x in obj.content.entrySet()
        }
    if jtype == km.DataTypes.TypeSpec.AGGREGATE and isinstance(
        obj.content, collections.abc.Iterable
    ):
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
