import os
import re
import sys
import urllib.request
import zipfile
from contextlib import contextmanager

import jpype

import pymafia.kolmafia.patch as patch
from pymafia import config
from pymafia.kolmafia import km

if sys.version_info >= (3, 11):
    # Added in Python 3.11
    from contextlib import chdir
else:

    @contextmanager
    def chdir(path: str):
        original_dir = os.getcwd()
        os.chdir(path)
        try:
            yield
        finally:
            os.chdir(original_dir)


GITHUB_DOWNLOAD_URL = "https://github.com/kolmafia/kolmafia/releases/download/"
JAVA_PATTERN = "(net\\/sourceforge\\/kolmafia.*\\/([^\\$]*))\\.class"

initializers = []


def on_kolmafia_start(func):
    global initializers
    initializers.append(func)
    return func


def download_kolmafia(revision: int, filename: str) -> None:
    jar_url = GITHUB_DOWNLOAD_URL + f"r{revision}/KoLmafia-{revision}.jar"
    urllib.request.urlretrieve(jar_url, filename=filename)


def start_kolmafia() -> None:
    jar_location = (
        config.kolmafia_directory / f"KoLmafia-{config.kolmafia_revision}.jar"
    )
    if not jar_location.is_file():
        config.kolmafia_directory.mkdir(parents=True, exist_ok=True)
        download_kolmafia(config.kolmafia_revision, jar_location)

    # KoLmafia will place its files in the current working directory, regardless of where the jar file is located.
    with chdir(config.kolmafia_directory):
        jpype.startJVM(classpath=str(jar_location), convertStrings=True)
    patch.apply()

    with zipfile.ZipFile(jar_location) as archive:
        for filename in archive.namelist():
            if match := re.search(JAVA_PATTERN, filename):
                km._jclass_names[match.group(2)] = match.group(1)

    for func in initializers:
        func()
