from pymafia.kolmafia import km

if not km.KoLmafia.permitsContinue():
    raise RuntimeError
