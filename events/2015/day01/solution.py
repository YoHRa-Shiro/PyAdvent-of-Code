from common.puzzle import Puzzle


class Puzzle1(Puzzle, part="part1"):
    @classmethod
    def solver(cls, puzzle_input: str | None) -> int:
        return puzzle_input.count("(") - puzzle_input.count(")")


class Puzzle2(Puzzle, part="part2"):
    @classmethod
    def solver(cls, puzzle_input: str) -> int:
        floor_level: int = 0

        for position, char in enumerate(puzzle_input):
            floor_level += 1 if "(" == char else -1
            if floor_level < 0:
                return position + 1

        return len(puzzle_input)


if __name__ == "__main__":
    Puzzle1.resolve()
    Puzzle2.resolve()
