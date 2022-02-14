from pymafia import ash
from pymafia.datatypes import Item
from pymafia.utils import get_property
from pymafia.utils import have as _have

item = Item("SongBoom™ BoomBox")

song_keywords = {
    "Eye of the Giger": "spooky",
    "Food Vibrations": "food",
    "Remainin' Alive": "dr",
    "These Fists Were Made for Punchin'": "damage",
    "Total Eclipse of Your Meat": "meat",
    "Silence": "off",
    None: "off",
}


def have():
    """Return True if the player has the SongBoom™ BoomBox available, False otherwise."""
    return _have(item)


def song():
    """Return the current SongBoom™ Boombox song."""
    return get_property("boomBoxSong") or None


def song_changes_left():
    """Return the number of SongBoom™ Boombox song changes left today."""
    return get_property("_boomBoxSongsLeft", int)


def set_song(new_song):
    """Change the SongBoom™ Boombox song."""
    if not have():
        raise RuntimeError("need a SongBoom™ BoomBox")
    if song() == new_song:
        return
    if song_changes_left() < 1:
        raise RuntimeError("out of song changes")

    ash.cli_execute(f"boombox {song_keywords[new_song]}")


def drop_progress():
    """Return the progress to next SongBoom™ Boombox drop (e.g. gathered meat-clip)."""
    return get_property("_boomBoxFights", int)
