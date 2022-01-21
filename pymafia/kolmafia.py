from os import path
from urllib import request
import json
import zipfile
import re
import jnius_config


JAR_LOCATION = "./kolmafia.jar"
JENKINS_JOB_URL = "https://ci.kolmafia.us/job/Kolmafia/lastSuccessfulBuild/"
JAVA_PATTERN = "(net\\/sourceforge\\/kolmafia.*\\/([^\\$]*))\\.class"


class KoLmafia:
    def __init__(self, location=JAR_LOCATION):
        if path.isfile(location) is False:
            self.download(location)

        # fmt: off
        jnius_config.set_classpath(location)
        from jnius import autoclass, cast # pylint: disable=import-outside-toplevel,no-name-in-module
        # fmt: on

        self.autoclass = autoclass
        self.cast = cast
        self.classes = {}
        with zipfile.ZipFile(location) as archive:
            for file in archive.filelist:
                filename = file.orig_filename
                match = re.search(JAVA_PATTERN, filename)
                if match:
                    self.classes[match.group(2)] = match.group(1)

    @staticmethod
    def download(location):
        with request.urlopen(JENKINS_JOB_URL + "/api/json") as response:
            data = json.loads(response.read().decode())
            jar_url = (
                JENKINS_JOB_URL + "artifact/" + data["artifacts"][0]["relativePath"]
            )
            request.urlretrieve(jar_url, filename=location)

    def __getattr__(self, key):
        if key in self.classes:
            return self.autoclass(self.classes[key])
        raise AttributeError(f"{type(self).__name__!r} object has no attribute {key!r}")


km = KoLmafia()
