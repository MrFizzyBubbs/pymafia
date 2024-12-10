"""Check that basic features work."""

import jpype

from pymafia import km, start_kolmafia

start_kolmafia()
if not (jpype.isJVMStarted() and km.KoLmafia.permitsContinue()):
    raise RuntimeError
