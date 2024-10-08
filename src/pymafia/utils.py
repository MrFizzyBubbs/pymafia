__all__ = ["launch_gui", "login", "abort", "log", "execute", "script"]

from html import escape
from typing import Any

from jpype import JClass

from pymafia.ash import from_java
from pymafia.kolmafia import km


def launch_gui():
    """Launch the KoLmafia GUI."""
    km.KoLmafia.main(["--GUI"])


def login(username: str, password: str | None = None) -> bool:
    """Login to Kingdom of Loathing through KoLmafia."""
    if password is None:
        password = km.KoLmafia.getSaveState(username)

    request = km.LoginRequest(username, password)
    request.run()
    return request


def abort(message: str = ""):
    """Immediately halt KoLmafia."""
    km.KoLmafia.updateDisplay(km.KoLConstants.MafiaState.ABORT, message)


def log(message: str, html: bool = False):
    """Log a message in the KoLmafia CLI."""
    message = str(message)
    if not html:
        message = escape(message)

    km.RequestLogger.printLine(message)


def execute(command: str) -> str:
    """Execute a command in the KoLmafia CLI and return the output."""
    JOutputStream = JClass("java.io.OutputStream")
    JByteArrayOutputStream = JClass("java.io.ByteArrayOutputStream")
    JPrintStream = JClass("java.io.PrintStream")

    ostream = JOutputStream @ JByteArrayOutputStream()
    out = JPrintStream(ostream)
    km.RequestLogger.openCustom(out)
    km.KoLmafiaCLI.DEFAULT_SHELL.executeLine(command)
    return ostream.toString()


def script(lines: str, convert=True) -> Any:
    """Execute an ash script and return the result, optionally converting it."""
    JString = JClass("java.lang.String")
    JByteArrayInputStream = JClass("java.io.ByteArrayInputStream")

    stream = JByteArrayInputStream(JString(lines).getBytes())
    interpreter = km.AshRuntime()
    interpreter.validate(None, stream)
    value = interpreter.execute("main", None)
    return from_java(value) if convert else value
