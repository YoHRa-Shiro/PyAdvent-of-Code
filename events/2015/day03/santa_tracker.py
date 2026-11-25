from dataclasses import replace

from common.puzzle import Puzzle
from dataclass.position import Position


class Puzzle1(Puzzle, part="part1"):
    @classmethod
    def solver(cls, puzzle_input: str | None) -> int:
        santa_position = Position(lat=0, long=0)
        places_visited = set([replace(santa_position)])

        for movement in puzzle_input:
            if "^" == movement:
                santa_position.long += 1
            elif "v" == movement:
                santa_position.long -= 1
            elif ">" == movement:
                santa_position.lat += 1
            elif "<" == movement:
                santa_position.lat -= 1
            places_visited.add(replace(santa_position))

        return len(places_visited)


class Puzzle2(Puzzle, part="part2"):
    @classmethod
    def solver(cls, puzzle_input: str) -> int:
        santa_position = Position(lat=0, long=0)
        santa_robot_position = Position(lat=0, long=0)
        places_visited = set([replace(santa_position)])

        for movement in puzzle_input[::2]:
            if "^" == movement:
                santa_position.long += 1
            elif "v" == movement:
                santa_position.long -= 1
            elif ">" == movement:
                santa_position.lat += 1
            elif "<" == movement:
                santa_position.lat -= 1
            places_visited.add(replace(santa_position))
        for movement in puzzle_input[1::2]:
            if "^" == movement:
                santa_robot_position.long += 1
            elif "v" == movement:
                santa_robot_position.long -= 1
            elif ">" == movement:
                santa_robot_position.lat += 1
            elif "<" == movement:
                santa_robot_position.lat -= 1
            places_visited.add(replace(santa_robot_position))

        return len(places_visited)


if __name__ == "__main__":
    Puzzle1.resolve()
    Puzzle2.resolve()
