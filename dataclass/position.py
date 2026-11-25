from dataclasses import dataclass


@dataclass
class Position:
    lat: int
    long: int

    def __eq__(self, position):
        return self.lat == position.lat and self.long == position.long

    def __hash__(self):
        return hash(self.lat + self.long)
