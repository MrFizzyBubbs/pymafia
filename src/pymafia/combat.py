from __future__ import annotations

from typing import Any

from pymafia.datatypes import Class, Effect, Item, Location, Monster, Skill, Stat

PreBALLSPredicate = (
    str | Monster | list[Monster] | Effect | Skill | Item | Location | Class | Stat
)


class Macro:
    def __init__(self, commands: list[str] | None = None):
        self.commands = commands or []

    def __str__(self) -> str:
        return ";".join(self.commands) + ";" if self.commands else ""

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.commands!r})"

    def __add__(self, other: Any) -> Macro:
        if isinstance(other, type(self)):
            return type(self)(self.commands + other.commands)
        return NotImplemented

    @classmethod
    def make_BALLS_predicate(cls, condition: PreBALLSPredicate) -> str:
        if isinstance(condition, Monster):
            return f"monsterid {condition.id}"
        if isinstance(condition, list):
            return " || ".join([cls.make_BALLS_predicate(x) for x in condition])
        if isinstance(condition, Effect):
            return f"haseffect {condition.id}"
        if isinstance(condition, Skill):
            return f"hasskill {condition.id}"
        if isinstance(condition, Item):
            if not condition.combat:
                raise ValueError(f"{condition!r} is not combat-usable")
            return f"hascombatitem {condition.id}"
        if isinstance(condition, Location):
            if condition.id < 1:
                raise ValueError(f"{condition!r} has no location id")
            return f"snarfblat {condition.id}"
        if isinstance(condition, Class):
            if condition.id > 6:
                raise ValueError(f"{condition!r} is not a standard class")
            return str(condition).replace(" ", "").lower()
        if isinstance(condition, Stat):
            return f"{str(condition).lower()}class"
        return condition

    def step(self, step: str | Macro) -> Macro:
        macro = Macro([step]) if isinstance(step, str) else step
        return self + macro

    def abort(self, message="") -> Macro:
        return self.step(f'abort "{message}"')

    def attack(self) -> Macro:
        return self.step("attack")

    def repeat(self) -> Macro:
        return self.step("repeat")

    def runaway(self) -> Macro:
        return self.step("runaway")

    def skill(self, skill) -> Macro:
        return self.step(f"skill {skill.id}")

    def try_skill(self, skill: Skill) -> Macro:
        return self.if_(skill, Macro().skill(skill))

    def item(self, item: Item) -> Macro:
        return self.step(f"use {item.id}")

    def items(self, item1: Item, item2: Item) -> Macro:
        return self.step(f"use {item1.id}, {item2.id}")

    def try_item(self, item: Item) -> Macro:
        return self.if_(item, Macro().item(item))

    def if_(self, condition: PreBALLSPredicate, if_true: str | Macro) -> Macro:
        return (
            self.step(f"if {self.make_BALLS_predicate(condition)}")
            .step(if_true)
            .step("endif")
        )

    def while_(self, condition: PreBALLSPredicate, if_true: str | Macro) -> Macro:
        return (
            self.step(f"while {self.make_BALLS_predicate(condition)}")
            .step(if_true)
            .step("endwhile")
        )
