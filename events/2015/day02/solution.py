from common.puzzle import Puzzle
from dataclass.box import Box


class Puzzle1(Puzzle, part="part1"):
    @classmethod
    def compute_paper_needed(cls, box: Box) -> int:
        return box.compute_surface_area() + box.compute_smallest_side_area()

    @classmethod
    def solver(cls, puzzle_input: str | None) -> int:
        total_paper_needed: int = 0

        for dimensions in puzzle_input.split(","):
            length, width, height = dimensions.split("x")
            box = Box(length=int(length), width=int(width), height=int(height))
            total_paper_needed += cls.compute_paper_needed(box)

        return total_paper_needed


class Puzzle2(Puzzle, part="part2"):
    @classmethod
    def compute_ribbon_needed(cls, box: Box) -> int:
        return box.compute_smallest_perimeter() + box.compute_volume()

    @classmethod
    def solver(cls, puzzle_input: str) -> int:
        total_ribbon_needed: int = 0

        for dimensions in puzzle_input.split(","):
            length, width, height = dimensions.split("x")
            box = Box(length=int(length), width=int(width), height=int(height))
            total_ribbon_needed += cls.compute_ribbon_needed(box)

        return total_ribbon_needed


if __name__ == "__main__":
    Puzzle1.resolve()
    Puzzle2.resolve()
