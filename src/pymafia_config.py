__all__ = ["set_revision", "set_location"]

import json
import os
import pathlib
import urllib.request
from typing import Literal

import jpype

GITHUB_RELEASE_URL = "https://api.github.com/repos/kolmafia/kolmafia/releases/"
RECOMMENDED_REVISION = int(pathlib.Path(".kolmafia-revision").read_text())

revision = RECOMMENDED_REVISION
location = os.path.join(os.getcwd(), "kolmafia")


def latest_revision() -> int:
    """Return the latest released version of KoLmafia."""
    with urllib.request.urlopen(GITHUB_RELEASE_URL + "latest") as response:
        data = json.loads(response.read().decode())
        return int(data["name"])


def check_jvm_running() -> None:
    """Raise an error if the JVM is running."""
    if jpype.isJVMStarted():
        raise RuntimeError("JVM is already running, can't change config")


def set_revision(rev: int | str | Literal["latest"]):
    """Set the revision of KoLmafia."""
    check_jvm_running()

    global revision
    revision = latest_revision() if rev == "latest" else int(rev)


def set_location(loc: str):
    """Set the location of KoLmafia."""
    check_jvm_running()

    global location
    location = os.path.join(os.getcwd(), loc)
