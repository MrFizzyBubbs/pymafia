import _jpype
import jpype
import wrapt

enabled = True


class KoLmafiaError(Exception):
    pass


# wrapt's wrap_function_wrapper does not allow specifying "enabled"
def wrap_function_wrapper(module, name, wrapper, enabled=None):
    return wrapt.wrap_object(
        module, name, wrapt.FunctionWrapper, (wrapper,), {"enabled": enabled}
    )


def apply():
    """Patch the JPype module to intercept all Java method calls.

    This patch does the following:
    * Automatically cast method arguments of type int to java.lang.Integer
    * Raise an exception if mafia is in a non-continue state after method invocation
    """
    KoLmafia = jpype.JClass("net.sourceforge.kolmafia.KoLmafia")

    def wrapper(wrapped, instance, args, kwargs):
        global enabled
        try:
            enabled = False

            args = [
                jpype.JInt(arg)
                if isinstance(arg, int) and not isinstance(arg, bool)
                else arg
                for arg in args
            ]
            result = wrapped(*args, **kwargs)

            if not KoLmafia.permitsContinue():
                KoLmafia.forceContinue()
                raise KoLmafiaError(KoLmafia.getLastMessage())

            return result
        finally:
            enabled = True

    wrap_function_wrapper(_jpype, "_JMethod.__call__", wrapper, enabled=lambda: enabled)
    wrap_function_wrapper(_jpype, "_JClass.__call__", wrapper, enabled=lambda: enabled)
