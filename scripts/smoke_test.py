from pymafia import km, start_kolmafia

start_kolmafia()
if not km.KoLmafia.permitsContinue():
    raise RuntimeError
