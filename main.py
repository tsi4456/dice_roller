import random
import re

DICE_REGEX = r"(?P<qty>\d+)d(?P<faces>\d+)"


class DiceGroup:
    def __init__(self, dice_string: str):
        self.parse(dice_string)

    def parse(self, dice_string: str) -> None:
        m = re.fullmatch(DICE_REGEX, dice_string)
        if not m:
            raise ValueError("Invalid dice string")
        self.qty = int(m["qty"])
        self.faces = int(m["faces"])

    def roll(self) -> list:
        return [random.randint(1, self.faces) for _ in range(self.qty)]


def main():
    dg = DiceGroup("4d6")
    print(dg.roll())


if __name__ == "__main__":
    main()
