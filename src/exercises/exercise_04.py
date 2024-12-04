import itertools
from typing import TYPE_CHECKING, Any

import attrs

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable


@attrs.define
class Exercise04:
    """Contains the solution to exercise 03 of the AoC 2024 challenge.

    Args:
        input_lines: An iterable of strings containing the input data.
    """

    input_lines: "Iterable[str]"

    def solve_part_1(self) -> int:
        """Solve the first part of the exercise.

        Returns:
            The result of the first part of the exercise.
        """
        char_grid = list(self.parsed_input_line())

        xmas_count = 0
        for y_coord in range(len(char_grid)):
            for x_coord in range(len(char_grid[0])):
                coords = (y_coord, x_coord)
                if char_grid[y_coord][x_coord] != "X":
                    continue
                for direction in gen_directions():
                    if direction_forms_xmas(coords, direction, char_grid):
                        xmas_count += 1
        return xmas_count

    def solve_part_2(self) -> int:
        """Solve the second part of the exercise.

        Returns:
            The result of the second part of the exercise.

        """
        char_grid = list(self.parsed_input_line())
        xmas_count = 0
        for y_coord in range(len(char_grid)):
            for x_coord in range(len(char_grid[0])):
                if is_center_of_xmas((y_coord, x_coord), char_grid):
                    xmas_count += 1
        return xmas_count

    def parsed_input_line(self) -> "Generator[str, Any]":
        """Parse the input lines and yield the results.

        Yields:
            The parsed input line.
        """
        for input_line in self.input_lines:
            yield input_line.strip()


def is_center_of_xmas(coords: tuple[int, int], char_grid: list[str]) -> bool:
    """Check if the given coordinates are the center of an X-MAS pattern.

    Args:
        coords: The coordinates of the center.
        char_grid: The grid of characters.

    Returns:
        True if the given coordinates are the center of a XMAS pattern, False otherwise.
    """
    if char_grid[coords[0]][coords[1]] != "A":
        return False
    direction_pairs = (((-1, -1), (1, 1)), ((1, -1), (-1, 1)))
    for direction_pair in direction_pairs:
        chars_at_directions = ""
        for direction in direction_pair:
            try:
                chars_at_directions += char_grid[coords[0] + direction[0]][
                    coords[1] + direction[1]
                ]
            except IndexError:
                return False

        if "M" not in chars_at_directions:
            return False
        if "S" not in chars_at_directions:
            return False
    return True


def direction_forms_xmas(
    starting_coords: tuple[int, int], direction: tuple[int, int], char_grid: list[str]
) -> bool:
    """Check if the given direction forms an XMAS pattern.

    Args:
        starting_coords: The coordinates to start from.(Of the X character)
        direction: The direction to check.
        char_grid: The grid of characters.

    Returns:
        True if the given direction forms an XMAS pattern, False otherwise.
    """
    coords = starting_coords

    for char_next_in_line in "MAS":
        coords = (coords[0] + direction[0], coords[1] + direction[1])
        if any(coord < 0 for coord in coords):
            return False

        try:
            char = char_grid[coords[0]][coords[1]]
        except IndexError:
            return False

        if char_next_in_line != char:
            return False
    return True


def gen_directions() -> "Generator[tuple[int,int], Any]":
    """Generate directions.

    Yields:
        The directions.
    """
    for y_direction, x_direction in itertools.product([1, -1, 0], repeat=2):
        if (y_direction, x_direction) == (0, 0):
            continue

        yield (y_direction, x_direction)


if __name__ == "__main__":
    import pathlib

    INPUT_FILE = pathlib.Path(".exercise_input/exercise_04.txt")
    with INPUT_FILE.open() as f:
        print(Exercise04(input_lines=f.readlines()).solve_part_1())  # noqa: T201  Might later be replaced with a proper CLI
        print(Exercise04(input_lines=f.readlines()).solve_part_2())  # noqa: T201
