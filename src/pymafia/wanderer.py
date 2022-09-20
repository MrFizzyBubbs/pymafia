from pymafia import ash
from pymafia.preference import get_property

WANDERER_HOLIDAYS = {
    "El Dia De Los Muertos Borrachos",
    "Feast of Boris",
    "Talk Like a Pirate Day",
}


def holiday_wanderer_day() -> bool:
    """Return whether today is a holiday wanderer day."""
    holidays_today = set(ash.holiday().split("/"))
    return bool(holidays_today.intersection(WANDERER_HOLIDAYS))


def vote_wanderer_now() -> float:
    """Returns whether the player will encounter a vote wanderer on the next
    turn, providing an "I Voted!" sticker is equipped."""
    return (
        ash.total_turns_played() % 11 == 1
        and get_property("lastVoteMonsterTurn", int) < ash.total_turns_played()
    )


def kramco_wanderer_chance() -> float:
    """Returns the chance the player will encounter a sausage goblin on the
    next turn, providing the Kramco Sausage-o-Matic is equipped."""
    fights = get_property("_sausageFights", int)
    last_fight = get_property("_lastSausageMonsterTurn", int)
    total_turns = ash.total_turns_played()
    if fights < 1:
        return last_fight == total_turns and 0.5 if ash.my_turncount() < 1 else 1.0
    turns_since_last_fight = total_turns - last_fight
    return min(
        1.0, (turns_since_last_fight + 1) / (5 + fights * 3 + max(0, fights - 5) ** 3)
    )
