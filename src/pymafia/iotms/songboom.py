from enum import Enum

from pymafia import ash, player
from pymafia.datatypes import Item
from pymafia.preference import get_property

ITEM = Item("SongBoom™ BoomBox")


class SongboomSong(str, Enum):
    SPOOKY = "Eye of the Giger"
    FOOD = "Food Vibrations"
    DR = "Remainin' Alive"
    DAMAGE = "These Fists Were Made for Punchin'"
    MEAT = "Total Eclipse of Your Meat"
    NONE = ""


def have() -> bool:
    """Return True if the player has the SongBoom™ BoomBox available, False otherwise."""
    return player.have(ITEM)


def current_song() -> SongboomSong:
    """Return the current SongBoom™ Boombox song."""
    return SongboomSong[get_property("boomBoxSong")]


def song_changes_left() -> int:
    """Return the number of SongBoom™ Boombox song changes left today."""
    return get_property("_boomBoxSongsLeft", int)


def set_song(song: SongboomSong) -> bool:
    """Change the SongBoom™ Boombox song."""
    if not have():
        return False
    if current_song() is song:
        return True
    if song_changes_left() < 1:
        return False

    return ash.cli_execute(f"boombox {song.value}")


def drop_progress() -> int:
    """Return the progress to next SongBoom™ Boombox drop (e.g. gathered meat-clip)."""
    return get_property("_boomBoxFights", int)
