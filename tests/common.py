import inspect


def get_property_names(cls):
    members = inspect.getmembers(cls, lambda x: isinstance(x, property))
    return [name for (name, _) in members]
