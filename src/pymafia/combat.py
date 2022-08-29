class Macro:
    def __init__(self, commands=None):
        self.commands = [] if commands is None else commands

    def __str__(self):
        return ";".join(self.commands) + ";" if self.commands else ""

    def __repr__(self):
        return f"{type(self).__name__}({self.commands!r})"

    def __add__(self, other):
        return type(self)(self.commands + other.commands)

    def step(self, steps):
        if isinstance(steps, str):
            return self + type(self)([steps])
        return self + steps

    def abort(self, message=""):
        return self.step(f'abort "{message}"')

    def attack(self):
        return self.step("attack")

    def repeat(self):
        return self.step("repeat")

    def runaway(self):
        return self.step("runaway")

    def skill(self, skill):
        return self.step(f"skill {skill.id}")

    def try_skill(self, skill):
        return self.step(f"if hasskill {skill.id}").skill(skill).step("endif")

    def item(self, item):
        return self.step(f"use {item.id}")

    def if_monster(self, monster, macro):
        return self.step(f"if monsterid {monster.id}").step(macro).step("endif")

    def check_monster(self, monsters):
        monsters = monsters if isinstance(monsters, list) else [monsters]
        predicate = " || ".join([f"monsterid {x.id}" for x in monsters])
        return self.step(f"if !({predicate})").abort("unexpected monster").step("endif")
