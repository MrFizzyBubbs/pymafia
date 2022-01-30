from pymafia.kolmafia import km
from pymafia.types import (
    Item,
    Location,
    Class,
    Stat,
    Skill,
    Effect,
    Familiar,
    Slot,
    Monster,
    Element,
    Coinmaster,
    Phylum,
    Thrall,
    Bounty,
    Servant,
    Vykea,
)


TreeMap = km.autoclass("java.util.TreeMap")
ArrayList = km.autoclass("java.util.ArrayList")
String = km.autoclass("java.lang.String")
ByteArrayInputStream = km.autoclass("java.io.ByteArrayInputStream")

simple_types = {
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
}


def __getattr__(name):
    return AshFunction(name)


def to_java(obj):
    if isinstance(obj, (type(None), int, float, str)):
        return km.Value(obj)
    if isinstance(obj, tuple(simple_types.values())):
        parse = getattr(km.DataTypes, f"parse{type(obj).__name__}Value")
        return parse(str(obj), False)
    if isinstance(obj, list):
        array_list = ArrayList()
        for value in obj:
            java_value = to_java(value)
            array_list.add(java_value)

        data_type = next(iter(array_list)).getType()
        size = array_list.size()
        return km.ArrayValue(km.AggregateType(data_type, size), array_list)
    if isinstance(obj, dict):
        tree_map = TreeMap()
        for key, value in obj.items():
            java_key = to_java(key)
            java_value = to_java(value)
            tree_map.put(java_key, java_value)

        data_type = tree_map.getFirstEntry().getValue().getType()
        index_type = tree_map.getFirstEntry().getKey().getType()
        return km.MapValue(km.AggregateType(data_type, index_type), tree_map)

    raise TypeError(f"unsupported argument type {type(obj).__name__!r}")


def from_java(obj):
    java_type = obj.getType().getType()
    if java_type in [km.DataTypes.TYPE_VOID, km.DataTypes.TYPE_ANY]:
        return None
    if java_type in simple_types:
        return simple_types[java_type](obj.toJSON())
    if java_type == km.DataTypes.TYPE_AGGREGATE and isinstance(obj.content, list):
        return [from_java(x) for x in obj.content]
    if java_type == km.DataTypes.TYPE_AGGREGATE and isinstance(obj.content, TreeMap):
        return {from_java(e.key): from_java(e.value) for e in obj.content.entrySet()}

    raise TypeError(
        f"unsupported return type {java_type!r}: {obj.getType().getName()!r}"
    )


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
    return value if raw else from_java(value)


class AshFunction:
    def __init__(self, name):
        self.name = name
        self.func = getattr(km.RuntimeLibrary, self.name)

    def __call__(self, *args, raw=False):
        interpreter = km.AshRuntime()
        value = self.func(interpreter, *[to_java(arg) for arg in args])
        return value if raw else from_java(value)

    @property
    def signatures(self):
        functions = km.RuntimeLibrary.getFunctions().findFunctions(self.name)
        return [f"{f.getType().toString()} {f.getSignature()}" for f in functions]

    @property
    def wiki(self):
        return f"https://wiki.kolmafia.us/index.php/{self.name}"
