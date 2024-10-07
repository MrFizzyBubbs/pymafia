import os
import re
import sys
import urllib.request
import zipfile
from collections.abc import Callable
from contextlib import contextmanager

import jpype

from pymafia import config
from pymafia.kolmafia import km
from pymafia.kolmafia.patch import patch_jpype

if sys.version_info >= (3, 11):
    # Added in Python 3.11
    from contextlib import chdir
else:

    @contextmanager
    def chdir(path: str) -> None:
        """Non thread-safe context manager to change the current working directory."""
        original_dir = os.getcwd()
        os.chdir(path)
        try:
            yield
        finally:
            os.chdir(original_dir)


JAVA_PATTERN = "(net\\/sourceforge\\/kolmafia.*\\/([^\\$]*))\\.class"

initializers: list[Callable] = []


def on_kolmafia_start(func: Callable) -> Callable:
    """Register a function to run when KoLmafia starts."""
    initializers.append(func)
    return func


def start_kolmafia() -> None:
    """Start KoLmafia by launching the JVM."""
    jar_name = f"KoLmafia-{config.kolmafia_revision}.jar"
    jar_location = config.kolmafia_directory / jar_name

    if not jar_location.is_file():
        config.kolmafia_directory.mkdir(parents=True, exist_ok=True)
        jar_url = f"https://github.com/kolmafia/kolmafia/releases/download/r{config.kolmafia_revision}/{jar_name}"
        urllib.request.urlretrieve(jar_url, filename=jar_location)

    # KoLmafia will place its files in the current working directory, regardless of where the jar file is located.
    with chdir(config.kolmafia_directory):
        jpype.startJVM(classpath=str(jar_location), convertStrings=True)

    patch_jpype()

    with zipfile.ZipFile(jar_location) as archive:
        for filename in archive.namelist():
            if match := re.search(JAVA_PATTERN, filename):
                km._jclass_names[match.group(2)] = match.group(1)

    for func in initializers:
        func()
