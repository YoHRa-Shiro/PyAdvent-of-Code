import os
import sys
from abc import ABC, abstractmethod

from common.puzzle_data import Example
from utils.enum import Colors
from utils.loader import load_data, load_lore
from utils.ustr import snake_to_tile_case


class Puzzle(ABC):
    def __init_subclass__(cls, *, part: str, **kwargs):
        super().__init_subclass__(**kwargs)

        module_file = sys.modules[cls.__module__].__file__
        cls.part = part
        cls.puzzle_data = load_data(module_file, part)

    @classmethod
    def input(cls) -> str:
        """Return the main puzzle input of the current puzzle"""
        return cls.puzzle_data.input

    @classmethod
    def examples(cls) -> list[Example]:
        """Return all examples of the current puzzle"""
        return cls.puzzle_data.examples

    @classmethod
    def display_lore(cls) -> None:
        """Display the lore of the current puzzle"""
        module_file = sys.modules[cls.__module__].__file__
        print(f"{Colors.GRAY}${load_lore(module_file, cls.part)}{Colors.RESET}")

    @classmethod
    @abstractmethod
    def solver(cls, puzzle_input: str) -> int:
        """Algorithm that solve the puzle for a given `puzzle_input`"""
        raise NotImplementedError("Missing function 'solvers' definition")

    @classmethod
    def solution(cls) -> int:
        """Display the solution of the current puzzle"""
        print(f"{Colors.CYAN}Solution for this problem: {Colors.BOLD}{Colors.RED}{cls.solver(cls.input())}{Colors.RESET}")

    @classmethod
    def verify(cls):
        """Test the solver algorithm with all given examples"""
        for example in cls.examples():
            computed_result = cls.solver(example.input)

            if example.result != computed_result:
                raise AssertionError(
                    f"Error in logic for example '{example.input}', expected '{example.result}' but result is '{computed_result}'"
                )

        print(f"  {Colors.GREEN}↪ {len(cls.examples())} examples passed successfully.{Colors.RESET}")

    @classmethod
    def resolve(cls, show_lore=False) -> None:
        """Pretty print the full problem lore, tests and solution"""
        file = os.path.basename(sys.modules[cls.__module__].__file__)

        print(f"{Colors.GRAY}--------{Colors.RESET}")
        print(f"{Colors.CYAN}Puzzle name: {Colors.MAGENTA}{snake_to_tile_case(file)} - {cls.part}{Colors.RESET}")
        if show_lore:
            cls.display_lore()
            print()
        cls.verify()
        cls.solution()
        print(f"{Colors.GRAY}--------{Colors.RESET}")
