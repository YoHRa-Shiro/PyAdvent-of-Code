from dataclasses import dataclass


@dataclass
class Box:
    length: int
    width: int
    height: int

    def get_smallest_sides(self):
        all_sides = [self.length, self.width, self.height]
        all_sides.remove(max(all_sides))
        return all_sides

    def compute_surface_area(self):
        return 2 * self.length * self.width + 2 * self.length * self.height + 2 * self.width * self.height

    def compute_smallest_side_area(self):
        smallest_sides = self.get_smallest_sides()
        return smallest_sides[0] * smallest_sides[1]

    def compute_smallest_perimeter(self):
        smallest_sides = self.get_smallest_sides()
        return 2 * smallest_sides[0] + 2 * smallest_sides[1]

    def compute_volume(self):
        return self.length * self.width * self.height
