import re
from html import escape

import pymafia.kolmafia as km
from pymafia import ash
from pymafia.datatypes import Effect, Familiar, Item, Monster, Servant, Skill

HOLIDAY_WANDERERS = {
    "El Dia De Los Muertos Borrachos": [
        Monster("Novia Cadáver"),
        Monster("Novio Cadáver"),
        Monster("Padre Cadáver"),
        Monster("Persona Inocente Cadáver"),
    ],
    "Feast of Boris": [
        Monster("Candied Yam Golem"),
        Monster("Malevolent Tofurkey"),
        Monster("Possessed Can of Cranberry Sauce"),
        Monster("Stuffing Golem"),
    ],
    "Talk Like a Pirate Day": [
        Monster("ambulatory pirate"),
        Monster("migratory pirate"),
        Monster("peripatetic pirate"),
    ],
}

ByteArrayOutputStream = km.autoclass("java.io.ByteArrayOutputStream")
PrintStream = km.autoclass("java.io.PrintStream")


def force_continue():
    km.autoclass("net/sourceforge/kolmafia/KoLmafia").forceContinue()


def launch_gui():
    km.KoLmafia.main(["--GUI"])


def login(username, password=None):
    if password is None:
        password = km.KoLmafia.getSaveState(username)

    request = km.LoginRequest(username, password)
    request.run()
    return request


def abort(message=None):
    km.KoLmafia.updateDisplay(km.KoLConstants.MafiaState.ABORT, message)


def log(message="", html=False):
    message = str(message)
    if not html:
        message = escape(message)

    km.RequestLogger.printLine(message)


def execute(command):
    ostream = km.cast("java.io.OutputStream", ByteArrayOutputStream())
    out = PrintStream(ostream)
    km.RequestLogger.openCustom(out)
    km.KoLmafiaCLI.DEFAULT_SHELL.executeLine(command)
    return ostream.toString()


def get_property(name, t=str):
    if t is bool:
        return km.Preferences.getBoolean(name)
    if t is int:
        return km.Preferences.getInteger(name)
    if t is float:
        return km.Preferences.getFloat(name)
    return t(km.Preferences.getString(name))


def set_property(name, value=""):
    if isinstance(value, bool):
        return km.Preferences.setBoolean(name, value)
    if isinstance(value, int):
        return km.Preferences.setInteger(name, value)
    if isinstance(value, float):
        return km.Preferences.setFloat(name, value)
    return km.Preferences.setString(name, str(value))


def have(thing, quantity=1):
    if isinstance(thing, Effect):
        return ash.have_effect(thing) >= quantity
    if isinstance(thing, Familiar):
        return ash.have_familiar(thing)
    if isinstance(thing, Item):
        return ash.available_amount(thing) >= quantity
    if isinstance(thing, Servant):
        return ash.have_servant(thing)
    if isinstance(thing, Skill):
        return ash.have_skill(thing)
    raise TypeError(f"unexpected type {type(thing).__name__!r}")


def in_choice(choice):
    return ash.handling_choice() and ash.last_choice() == choice


def in_combat(monster=None):
    if ash.current_round() < 1:
        return False
    if monster is None:
        return True

    page = ash.visit_url("fight.php")
    match = re.search("<!-- MONSTERID: (\\d+) -->", page)
    if not match:
        raise RuntimeError("unable to identify monster")
    return int(match.group(1)) == monster.id


def can_kmail():
    return not (
        ash.current_round() > 0  # In a fight
        or ash.handling_choice()  # In a choice
        or ash.fight_follows_choice()  # Was in a choice, gonna be in a fight
        or ash.choice_follows_fight()  # Was in a fight, gonna be in a choice
        or ash.in_multi_fight()  # Was in a fight, gonna be in another fight
    )


def try_use(item):
    if have(item):
        ash.use(1, item)


def get_todays_holiday_wanderers():
    today = ash.holiday()
    if not today:
        return []
    return [mon for holiday in today for mon in HOLIDAY_WANDERERS[holiday.split("/")]]
