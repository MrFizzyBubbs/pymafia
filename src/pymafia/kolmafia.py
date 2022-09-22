import json
import os
import re
import sys
import urllib.request
import zipfile
from typing import Any

import jnius_config

JAR_LOCATION = "./kolmafia.jar"
JENKINS_JOB_URL = "https://ci.kolmafia.us/job/Kolmafia/lastSuccessfulBuild/"
JAVA_PATTERN = "(net\\/sourceforge\\/kolmafia.*\\/([^\\$]*))\\.class"


class MafiaError(Exception):
    pass


class KoLmafia:
    autoclass: Any
    cast: Any
    classes: dict[str, Any]

    def __init__(self, location: str = JAR_LOCATION):
        if not os.path.isfile(location):
            self.download(location)

        jnius_config.set_classpath(location)
        from jnius import autoclass, cast

        self.autoclass = autoclass
        self.cast = cast

        self.classes = {}
        with zipfile.ZipFile(location) as archive:
            for file in archive.filelist:
                filename = file.orig_filename
                match = re.search(JAVA_PATTERN, filename)
                if match:
                    self.classes[match.group(2)] = match.group(1)

    def __getattr__(self, key: str) -> Any:
        if key in self.classes:
            return self.autoclass(self.classes[key])
        return self.autoclass(f"net.sourceforge.kolmafia.{key}")

    @staticmethod
    def download(location: str) -> None:
        with urllib.request.urlopen(JENKINS_JOB_URL + "/api/json") as response:
            data = json.loads(response.read().decode())
            jar_url = (
                JENKINS_JOB_URL + "artifact/" + data["artifacts"][0]["relativePath"]
            )
            urllib.request.urlretrieve(jar_url, filename=location)


km = KoLmafia()


def tracer(frame, event, arg):
    """Monitor return events for a mafia error.

    See https://stackoverflow.com/questions/59088671/hooking-every-function-call-in-python.
    """
    if event == "call":
        # disable per-line events on the frame to improve performance
        frame.f_trace_lines = False
        return tracer

    elif event == "return":
        if not km.KoLmafia.permitsContinue():
            km.KoLmafia.forceContinue()
            raise MafiaError(km.KoLmafia.getLastMessage())


sys.settrace(tracer)
