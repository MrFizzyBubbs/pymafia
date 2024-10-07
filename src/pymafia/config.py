__all__ = ["set_kolmafia_revision", "set_kolmafia_directory"]

import json
import os
import urllib.request
from pathlib import Path
from typing import Literal

import jpype

GITHUB_RELEASE_URL = "https://api.github.com/repos/kolmafia/kolmafia/releases/"
RECOMMENDED_REVISION = int(Path(".kolmafia-revision").read_text())
DEFAULT_DIRECTORY = Path.cwd() / "kolmafia"

kolmafia_revision = RECOMMENDED_REVISION
kolmafia_directory = DEFAULT_DIRECTORY


def check_jvm_running() -> None:
    """Raise an error if the JVM is running."""
    if jpype.isJVMStarted():
        raise RuntimeError("JVM is already running, can not change config")


def latest_kolmafia_revision() -> int:
    """Return the latest released version of KoLmafia."""
    with urllib.request.urlopen(GITHUB_RELEASE_URL + "latest") as response:
        data = json.loads(response.read().decode())
        return int(data["name"])


def set_kolmafia_revision(revision: int | str | Literal["latest"]) -> None:
    """Set the revision of KoLmafia to use."""
    check_jvm_running()

    global kolmafia_revision
    if revision == "latest":
        kolmafia_revision = latest_kolmafia_revision()
    else:
        kolmafia_revision = int(revision)


def set_kolmafia_directory(path: str | os.PathLike) -> None:
    """Set the directory to run the KoLmafia jar file in."""
    check_jvm_running()

    global kolmafia_directory
    kolmafia_directory = Path(path)
