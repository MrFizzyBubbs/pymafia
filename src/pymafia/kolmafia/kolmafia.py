import json
import os
import re
import urllib.request
import zipfile
from typing import Any, Iterable

import jpype

from pymafia.kolmafia import patch

JENKINS_JOB_URL = "https://ci.kolmafia.us/job/Kolmafia/lastSuccessfulBuild/"
JAR_LOCATION = "./kolmafia.jar"
JAVA_PATTERN = "(net\\/sourceforge\\/kolmafia.*\\/([^\\$]*))\\.class"


def download_kolmafia(location: str):
    with urllib.request.urlopen(JENKINS_JOB_URL + "/api/json") as response:
        data = json.loads(response.read().decode())
        jar_url = JENKINS_JOB_URL + "artifact/" + data["artifacts"][0]["relativePath"]
        urllib.request.urlretrieve(jar_url, filename=location)


class KoLmafia:
    def __init__(self, location: str):
        if not os.path.isfile(location):
            download_kolmafia(location)

        jpype.startJVM(classpath=location, convertStrings=True)
        patch.apply()

        self._classes = {}
        with zipfile.ZipFile(location) as archive:
            for filename in archive.namelist():
                if match := re.search(JAVA_PATTERN, filename):
                    self._classes[match.group(2)] = match.group(1)

    def __dir__(self) -> Iterable[str]:
        return list(self._classes.keys())

    def __getattr__(self, name: str) -> Any:
        if name in self._classes:
            return jpype.JClass(self._classes[name])
        return super().__getattribute__(name)


km = KoLmafia(JAR_LOCATION)
