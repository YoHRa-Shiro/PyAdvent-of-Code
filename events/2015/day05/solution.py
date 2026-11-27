from common.puzzle import Puzzle


class Puzzle1(Puzzle, part="part1"):
    @classmethod
    def is_nice(cls, input_string: str) -> bool:
        banned_substrings = ("ab", "cd", "pq", "xy")
        if any(banned_substring in input_string for banned_substring in banned_substrings):
            return False

        if not any(input_string[i] == input_string[i + 1] for i in range(0, len(input_string) - 1)):
            return False

        vowels = "aeiou"
        if 3 > len(list(filter(lambda letter: letter in vowels, input_string))):
            return False

        return True

    @classmethod
    def solver(cls, puzzle_input: str | None) -> int:
        nb_nice = 0
        for string in puzzle_input.split(","):
            nb_nice += cls.is_nice(string)
        return nb_nice


class Puzzle2(Puzzle, part="part2"):
    @classmethod
    def is_nice(cls, input_string: str) -> bool:
        if not any(input_string[i] == input_string[i + 2] for i in range(0, len(input_string) - 2)):
            return False

        return any(len(input_string) - len(input_string.replace(input_string[i : i + 2], "")) >= 4 for i in range(len(input_string) - 1))

    @classmethod
    def solver(cls, puzzle_input: str) -> int:
        nb_nice = 0
        for string in puzzle_input.split(","):
            nb_nice += cls.is_nice(string)
        return nb_nice


if __name__ == "__main__":
    Puzzle1.resolve()
    Puzzle2.resolve()
