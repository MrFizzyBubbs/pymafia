import json
import os
import re
import sys
import urllib
import zipfile

import jnius_config

JAR_LOCATION = "./kolmafia.jar"
JENKINS_JOB_URL = "https://ci.kolmafia.us/job/Kolmafia/lastSuccessfulBuild/"
JAVA_PATTERN = "(net\\/sourceforge\\/kolmafia.*\\/([^\\$]*))\\.class"


def download(location):
    with urllib.request.urlopen(JENKINS_JOB_URL + "/api/json") as response:
        data = json.loads(response.read().decode())
        jar_url = JENKINS_JOB_URL + "artifact/" + data["artifacts"][0]["relativePath"]
        urllib.request.urlretrieve(jar_url, filename=location)


if not os.path.isfile(JAR_LOCATION):
    download(JAR_LOCATION)
jnius_config.set_classpath(JAR_LOCATION)
from jnius import autoclass, cast  # pylint: disable=C0413,E0611,W0611

classes = {}
with zipfile.ZipFile(JAR_LOCATION) as archive:
    for file in archive.filelist:
        filename = file.orig_filename
        match = re.search(JAVA_PATTERN, filename)
        if match:
            classes[match.group(2)] = match.group(1)


def __getattr__(key):
    return autoclass(classes[key]) if key in classes else autoclass(key)


class MafiaError(Exception):
    pass


def tracer(frame, event, arg):
    """Monitor return events for a mafia error.

    See https://stackoverflow.com/questions/59088671/hooking-every-function-call-in-python.
    """
    if event == "call":
        # disable per-line events on the frame to improve performance
        frame.f_trace_lines = False
        return tracer

    elif event == "return":
        KoLmafia = autoclass("net/sourceforge/kolmafia/KoLmafia")
        if not KoLmafia.permitsContinue():
            KoLmafia.forceContinue()
            raise MafiaError(KoLmafia.getLastMessage())


sys.settrace(tracer)
