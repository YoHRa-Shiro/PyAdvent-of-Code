import hashlib

from common.puzzle import Puzzle


class Puzzle1(Puzzle, part="part1"):
    @classmethod
    def solver(cls, puzzle_input: str | None) -> int:
        salt = 0
        while not hashlib.md5(f"{puzzle_input}{salt}".encode()).hexdigest().startswith("00000"):
            salt += 1
        return salt


class Puzzle2(Puzzle, part="part2"):
    @classmethod
    def solver(cls, puzzle_input: str) -> int:
        salt = 0
        while not hashlib.md5(f"{puzzle_input}{salt}".encode()).hexdigest().startswith("000000"):
            salt += 1
        return salt


if __name__ == "__main__":
    Puzzle1.resolve()
    Puzzle2.resolve()
