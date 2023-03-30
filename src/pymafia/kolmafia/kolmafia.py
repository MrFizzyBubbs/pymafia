import re
import zipfile

from pymafia.kolmafia.jvm import JAR_LOCATION, jnius
from pymafia.kolmafia.proxy import JniusProxy

JAVA_PATTERN = "(net\\/sourceforge\\/kolmafia.*\\/([^\\$]*))\\.class"


class KoLmafia:
    def __init__(self, location: str):
        self.autoclass = JniusProxy(jnius.autoclass)
        self.cast = JniusProxy(jnius.cast)

        self.classes = {}
        with zipfile.ZipFile(location) as archive:
            for file in archive.filelist:
                filename = file.orig_filename
                if match := re.search(JAVA_PATTERN, filename):
                    self.classes[match.group(2)] = match.group(1)

    def __getattr__(self, name: str) -> JniusProxy:
        if name in self.classes:
            return self.autoclass(self.classes[name])
        return self.autoclass(f"net.sourceforge.kolmafia.{name}")


km = KoLmafia(JAR_LOCATION)
