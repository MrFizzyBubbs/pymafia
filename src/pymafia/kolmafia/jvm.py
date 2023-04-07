import json
import os
import urllib.request

import jnius_config

JAR_LOCATION = "./kolmafia.jar"
JENKINS_JOB_URL = "https://ci.kolmafia.us/job/Kolmafia/lastSuccessfulBuild/"


def download_kolmafia(location: str):
    with urllib.request.urlopen(JENKINS_JOB_URL + "/api/json") as response:
        data = json.loads(response.read().decode())
        jar_url = JENKINS_JOB_URL + "artifact/" + data["artifacts"][0]["relativePath"]
        urllib.request.urlretrieve(jar_url, filename=location)


if not os.path.isfile(JAR_LOCATION):
    download_kolmafia(JAR_LOCATION)
jnius_config.set_classpath(JAR_LOCATION)

import jnius  # Start the JVM

jnius.protocol_map["java.lang.Enum"] = {"__hash__": lambda self: self.hashCode()}
