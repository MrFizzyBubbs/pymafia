import json
import os
import re
import urllib.request
import zipfile
from typing import Any, Iterable

import jpype

import pymafia.kolmafia.patch as patch

GITHUB_RELEASE_URL = "https://api.github.com/repos/kolmafia/kolmafia/releases/"
GITHUB_DOWNLOAD_URL = "https://github.com/kolmafia/kolmafia/releases/download/"
JAVA_PATTERN = "(net\\/sourceforge\\/kolmafia.*\\/([^\\$]*))\\.class"


def latest_revision() -> str:
    with urllib.request.urlopen(GITHUB_RELEASE_URL + "latest") as response:
        data = json.loads(response.read().decode())
        return data["name"]


def download_kolmafia(revision: str, location: str):
    jar_url = GITHUB_DOWNLOAD_URL + f"r{revision}/KoLmafia-{revision}.jar"
    urllib.request.urlretrieve(jar_url, filename=location)


class KoLmafia:
    def __init__(self, revision: str):
        revision = latest_revision() if revision == "latest" else revision
        location = f"KoLmafia-{revision}.jar"

        if not os.path.isfile(location):
            download_kolmafia(revision, location)

        jpype.startJVM(classpath=location, convertStrings=True)
        patch.apply()

        self.classes = {}
        with zipfile.ZipFile(location) as archive:
            for filename in archive.namelist():
                if match := re.search(JAVA_PATTERN, filename):
                    self.classes[match.group(2)] = match.group(1)

    def __dir__(self) -> Iterable[str]:
        return sorted(list(self.classes.keys()))

    def __getattr__(self, name: str) -> Any:
        if name in self.classes:
            return jpype.JClass(self.classes[name])
        return super().__getattribute__(name)


km = KoLmafia(os.environ.get("KOLMAFIA_REVISION", "27467"))
