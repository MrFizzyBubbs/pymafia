__all__ = ["set_revision"]

import json
import urllib.request

GITHUB_RELEASE_URL = "https://api.github.com/repos/kolmafia/kolmafia/releases/"
MINIMUM_REVISION = 27467

revision = MINIMUM_REVISION


def latest_revision() -> int:
    with urllib.request.urlopen(GITHUB_RELEASE_URL + "latest") as response:
        data = json.loads(response.read().decode())
        return int(data["name"])


def set_revision(rev: int | str):
    global MINIMUM_REVISION, revision
    rev = latest_revision() if rev == "latest" else int(rev)
    if rev < MINIMUM_REVISION:
        raise ValueError(
            f"invalid revision {rev}, must be {MINIMUM_REVISION} or higher"
        )
    revision = rev
