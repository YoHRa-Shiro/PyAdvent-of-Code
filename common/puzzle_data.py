from dataclasses import dataclass


@dataclass
class Example:
    input: str
    result: int


@dataclass
class PuzzleData:
    input: str
    examples: list[Example]

    def __post_init__(self):
        self.examples = [Example(**e) if isinstance(e, dict) else e for e in self.examples]
