import os
import re
import sys
import urllib.request
import zipfile
from contextlib import contextmanager
from typing import Any, Iterable

import jpype

import pymafia.kolmafia.patch as patch
from pymafia import config

GITHUB_DOWNLOAD_URL = "https://github.com/kolmafia/kolmafia/releases/download/"
JAVA_PATTERN = "(net\\/sourceforge\\/kolmafia.*\\/([^\\$]*))\\.class"

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


def download_kolmafia(revision: int, filename: str):
    jar_url = GITHUB_DOWNLOAD_URL + f"r{revision}/KoLmafia-{revision}.jar"
    urllib.request.urlretrieve(jar_url, filename=filename)


class KoLmafia:
    _jclasses = {}
    # def __init__(self):
    #     jar_location = os.path.join(location, f"KoLmafia-{revision}.jar")
    #     os.makedirs(location, exist_ok=True)
    #     if not os.path.isfile(jar_location):
    #         download_kolmafia(revision, jar_location)

    #     # KoLmafia will place its files in the current working directory, regardless of where the jar file is located.
    #     with chdir(location):
    #         jpype.startJVM(classpath=jar_location, convertStrings=True)
    #     patch.apply()

    #     self.classes = {}
    #     with zipfile.ZipFile(jar_location) as archive:
    #         for filename in archive.namelist():
    #             if match := re.search(JAVA_PATTERN, filename):
    #                 self.classes[match.group(2)] = match.group(1)

    def __dir__(self) -> Iterable[str]:
        return sorted(list(self._jclasses.keys()))

    def __getattr__(self, name: str) -> Any:
        if name in self._jclasses:
            return jpype.JClass(self._jclasses[name])
        return super().__getattribute__(name)


km = KoLmafia()

initializers = []


def on_kolmafia_start(func):
    initializers.append(func)
    return func


def start() -> None:
    jar_location = (
        config.kolmafia_directory / f"KoLmafia-{config.kolmafia_revision}.jar"
    )
    if not jar_location.is_file():
        config.kolmafia_directory.mkdir(parents=True, exist_ok=True)
        download_kolmafia(config.kolmafia_revision, jar_location)

    # KoLmafia will place its files in the current working directory, regardless of where the jar file is located.
    with chdir(config.kolmafia_directory):
        print(jar_location)
        jpype.startJVM(classpath=str(jar_location), convertStrings=True)
    patch.apply()

    with zipfile.ZipFile(jar_location) as archive:
        for filename in archive.namelist():
            if match := re.search(JAVA_PATTERN, filename):
                km._jclasses[match.group(2)] = match.group(1)

    for func in initializers:
        func()
