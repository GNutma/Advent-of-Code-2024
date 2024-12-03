import collections
import pathlib
from typing import TYPE_CHECKING, Any

import attrs

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable


@attrs.define
class Exercise01:
    """Contains the solution to exercise 01 of the AoC 2024 challenge.

    Args:
        input_lines: An iterable of strings containing the input data.
    """

    input_lines: "Iterable[str]"

    def solve_part_1(self) -> int:
        """Solve the first part of the exercise.

        Returns:
            The result of the first part of the exercise.
        """
        first_array, second_array = self.parsed_data_to_list()

        sum_of_differences = 0
        for a, b in zip(sorted(first_array), sorted(second_array), strict=True):
            sum_of_differences += abs(a - b)
        return sum_of_differences

    def solve_part_2(self) -> int:
        """Solve the second part of the exercise.

        Returns:
            The result of the first part of the exercise.
        """
        first_array, second_array = self.parsed_data_to_list()
        occurrences = collections.Counter(second_array)
        similarity_score_sum = 0
        for value in first_array:
            similarity = value * occurrences[value]
            similarity_score_sum += similarity
        return similarity_score_sum

    def parsed_data_to_list(self) -> tuple[list[int], list[int]]:
        """Parse the input lines into a tuple of two lists of integers.

        Returns:
            A tuple of two lists of
        """
        first_array, second_array = [], []
        for first_value, second_value in self.parsed_input_line():
            first_array.append(int(first_value))
            second_array.append(int(second_value))
        return first_array, second_array

    def parsed_input_line(self) -> "Generator[list[str], Any]":
        """Parse the input lines and yield the results.

        Yields:
            The parsed input line.
        """
        for input_line in self.input_lines:
            yield input_line.strip().split()


if __name__ == "__main__":
    import pathlib

    INPUT_FILE = pathlib.Path(".exercise_input/exercise_01.txt")
    with INPUT_FILE.open() as f:
        print(Exercise01(input_lines=f.readlines()).solve_part_1())  # noqa: T201 # Might later be replaced with a proper CLI
        print(Exercise01(input_lines=f.readlines()).solve_part_2())  # noqa: T201
