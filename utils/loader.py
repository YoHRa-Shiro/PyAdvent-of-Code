import json
import os
from typing import TextIO

from common.puzzle_data import PuzzleData


def open_file(caller_file: str, filename: str) -> TextIO:
    """Open file from wherever the method was called."""
    path = os.path.join(os.path.dirname(caller_file), filename)
    return open(path, encoding="utf-8")


def load_data(caller_file: str, part: str) -> PuzzleData:
    """Load puzzle input file."""
    with open_file(caller_file, f"_inputs_{part}.json") as f:
        return PuzzleData(**json.load(f))


def load_lore(caller_file: str, part: str) -> str:
    """Load puzzle lore file."""
    with open_file(caller_file, f"_lore_{part}.txt") as f:
        return f.read()
