import jpype

from pymafia import start_kolmafia

if not jpype.isJVMStarted():
    start_kolmafia()
