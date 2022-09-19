import pymafia.kolmafia as km


class Path:
    id = 0
    name = "none"
    ascension_path = None

    def __init__(self, key=None):
        if key in (None, self.id, self.name):
            return

        ascension_path = km.AscensionPath.nameToPath(key) if isinstance(key, str) else km.AscensionPath.idToPath(key)

        if ascension_path == km.autoclass("net/sourceforge/kolmafia/AscensionPath$Path").NONE:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        self.id = ascension_path.getId()
        self.name = ascension_path.getName()
        self.ascension_path = ascension_path

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __hash__(self):
        return hash((self.id, self.name))

    def __eq__(self, other):
        return isinstance(other, type(self)) and (self.id, self.name) == (
            other.id,
            other.name,
        )

    def __bool__(self):
        return (self.id, self.name) != (type(self).id, type(self).name)

    @classmethod
    def all(cls):
        from pymafia import ash

        values = km.DataTypes.PATH_TYPE.allValues()
        return sorted(ash.to_python(values), key=lambda x: x.id)

    @property
    def avatar(self):
        return self.ascension_path.isAvatar()

    @property
    def image(self):
        return self.ascension_path.getImage()

    @property
    def points(self):
        return self.ascension_path.getPoints()

    @property
    def familiars(self):
        return self.ascension_path.canUseFamiliars()