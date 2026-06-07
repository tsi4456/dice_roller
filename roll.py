import random
import re
import sys
import time

DICE_REGEX = r"(?P<qty>\d+)d(?P<faces>\d+)(?P<static>(\+|\-)\d+)?(?P<mod>(t|b)\d+)?"
ROLL_DELAY_SECONDS = 1


class DiceGroup:
    def __init__(self, dice_string: str):
        self.parse(dice_string)
        self.dropped_dice = []
        self.roll()

    @property
    def total(self):
        return sum(self.results) + self.static_mods

    def __str__(self):
        return f"{str(self.results)}{str(self.dropped_dice) if self.dropped_dice else ''} {'+' if self.static_mods > 0 else ''}{self.static_mods if self.static_mods else ''}: {self.total}"

    def parse(self, dice_string: str) -> None:
        m = re.fullmatch(DICE_REGEX, dice_string)
        if m:
            self.static_mods = int(m["static"]) if m.groupdict().get("static") else 0
            self.group_mod = (m["mod"][0], int(m["mod"][1:])) if m["mod"] else None
        else:
            raise ValueError(
                "Invalid dice string - input should be in the form [X]d[Y](+|-Z)"
            )
        self.qty = int(m["qty"])
        self.faces = int(m["faces"])

    def roll(self) -> list:
        # animation = "|/-\\"
        idx = 0
        while idx < ROLL_DELAY_SECONDS * 10:
            print(
                f"{[random.randint(1, self.faces) for _ in range(self.qty)]}", end="\r"
            )
            # print(animation[idx % len(animation)], end="\r")
            idx += 1
            time.sleep(0.1)
        self.results = [random.randint(1, self.faces) for _ in range(self.qty)]
        print(self)


def main():
    args = sys.argv
    if len(args) > 1:
        try:
            groups = [DiceGroup(a) for a in args[1:]]
        except ValueError as e:
            print(e)
        print(f"Total: {sum([r.total for r in groups])}")
        # print(f"{'\n'.join(str(g) for g in groups)}")
    else:
        while True:
            prompt = input("> ")
            if not prompt:
                break
            try:
                groups = [DiceGroup(a) for a in prompt.split()]
            except ValueError as e:
                print(e)
            print(f"{'\n'.join(str(g) for g in groups)}")


if __name__ == "__main__":
    main()
