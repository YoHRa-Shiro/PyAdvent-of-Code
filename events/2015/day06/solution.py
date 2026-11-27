import re

import numpy as np

from common.puzzle import Puzzle


class Puzzle1(Puzzle, part="part1"):
    """
    One nice property: if I turn on a light, no matter what happens previously, the light is on now.
    -> so we can ignore every previous instructions for this light.
    -> same logic for turning off. If I turn off the light now, I can ignore every previous turn on/off/toggle.

    Not sure if I can do something nice about that fact. Let's just brute force the problem right now.
    """

    @classmethod
    def solver(cls, puzzle_input: str | None) -> int:
        lighting_grid = np.full((1000, 1000), False, dtype=bool)

        instructions = puzzle_input.split(";")
        for instruction in instructions:
            start1, start2, end1, end2 = list(map(int, re.findall(r"\d+", instruction)))
            end1 += 1
            end2 += 1

            if instruction.startswith("turn on"):
                lighting_grid[start1:end1, start2:end2] = True
            elif instruction.startswith("turn off"):
                lighting_grid[start1:end1, start2:end2] = False
            else:
                lighting_grid[start1:end1, start2:end2] = ~lighting_grid[start1:end1, start2:end2]

        return int(np.count_nonzero(lighting_grid))


class Puzzle2(Puzzle, part="part2"):
    @classmethod
    def solver(cls, puzzle_input: str) -> int:
        lighting_grid = np.zeros((1000, 1000), dtype=int)

        instructions = puzzle_input.split(";")
        for instruction in instructions:
            start1, start2, end1, end2 = list(map(int, re.findall(r"\d+", instruction)))
            end1 += 1
            end2 += 1

            if instruction.startswith("turn on"):
                lighting_grid[start1:end1, start2:end2] += 1
            elif instruction.startswith("turn off"):
                lighting_grid[start1:end1, start2:end2] -= 1
                lighting_grid[lighting_grid < 0] = 0  # cannot go lower than 0 (definitively not miss this rule the first time...)
            else:
                lighting_grid[start1:end1, start2:end2] += 2

        return lighting_grid.sum()


if __name__ == "__main__":
    Puzzle1.resolve()
    Puzzle2.resolve()
