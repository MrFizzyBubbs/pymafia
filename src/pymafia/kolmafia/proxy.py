import inspect

import wrapt

from pymafia.kolmafia.jvm import jnius

KoLmafia = jnius.autoclass("net.sourceforge.kolmafia.KoLmafia")
jnius_classes = tuple(x[1] for x in inspect.getmembers(jnius, inspect.isclass))


class MafiaError(Exception):
    pass


class JniusProxy(wrapt.ObjectProxy):
    def __call__(self, *args, **kwargs):
        try:
            args = tuple(self.unwrap(arg) for arg in args)
            kwargs = {key: self.unwrap(value) for key, value in kwargs.items()}
            return self.wrap(self.__wrapped__(*args, **kwargs))
        finally:
            if not KoLmafia.permitsContinue():
                KoLmafia.forceContinue()
                raise MafiaError(KoLmafia.getLastMessage())

    def __getattr__(self, name):
        return self.wrap(getattr(self.__wrapped__, name))

    def __hash__(self):
        return hash(self.__wrapped__)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.__wrapped__ == other.__wrapped__
        return NotImplemented

    @classmethod
    def wrap(cls, value):
        if isinstance(value, list):
            return [cls.wrap(x) for x in value]
        if not isinstance(value, cls) and isinstance(value, jnius_classes):
            return cls(value)
        return value

    @classmethod
    def unwrap(cls, value):
        if isinstance(value, list):
            return [cls.unwrap(x) for x in value]
        if isinstance(value, cls):
            return value.__wrapped__
        return value
