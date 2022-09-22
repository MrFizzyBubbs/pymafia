from html import escape

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
    MafiaState = getattr(km, "KoLConstants$MafiaState")
    km.KoLmafia.updateDisplay(MafiaState.ABORT, message)


def log(message: str, html: bool = False):
    """Log a message in the KoLmafia CLI."""
    message = str(message)
    if not html:
        message = escape(message)

    km.RequestLogger.printLine(message)


def execute(command: str) -> str:
    """Execute a command in the KoLmafia CLI and return the output."""
    ByteArrayOutputStream = km.autoclass("java.io.ByteArrayOutputStream")
    PrintStream = km.autoclass("java.io.PrintStream")

    ostream = km.cast("java.io.OutputStream", ByteArrayOutputStream())
    out = PrintStream(ostream)
    km.RequestLogger.openCustom(out)
    km.KoLmafiaCLI.DEFAULT_SHELL.executeLine(command)
    return ostream.toString()
