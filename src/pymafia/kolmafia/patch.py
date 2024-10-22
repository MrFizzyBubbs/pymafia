from typing import Any

import _jpype
import jpype
import wrapt

enabled = True


class KoLmafiaError(RuntimeError):
    pass


def int_to_jint(value: Any) -> Any:
    """Cast to JInt if the argument is an int, else return unchanged."""
    if isinstance(value, int) and not isinstance(value, bool):
        return jpype.JInt(value)
    return value


def patch_jpype() -> None:
    """Patch the JPype module to intercept all Java method calls.

    This patch does the following:
    * Automatically cast method arguments of type int to java.lang.Integer
    * Raise an exception if mafia is in a non-continue state after method invocation
    """
    JKoLmafia = jpype.JClass("net.sourceforge.kolmafia.KoLmafia")

    def wrapper(wrapped, instance, args, kwargs):
        global enabled
        try:
            enabled = False

            jargs = tuple(int_to_jint(arg) for arg in args)
            # _jpype does not support keyword arguments in method calls
            result = wrapped(*jargs)

            if not JKoLmafia.permitsContinue():
                JKoLmafia.forceContinue()
                raise KoLmafiaError(JKoLmafia.getLastMessage())

            return result
        finally:
            enabled = True

    for name in ["_JMethod.__call__", "_JClass.__call__"]:
        wrapt.patch_function_wrapper(_jpype, name, enabled=lambda: enabled)(wrapper)
