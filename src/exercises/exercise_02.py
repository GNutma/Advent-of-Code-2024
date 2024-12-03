from typing import TYPE_CHECKING, Any

import attrs

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable

MAX_DIFFERENCE_BETWEEN_REPORT_NUMBERS = 3


@attrs.define
class Exercise02:
    """Contains the solution to exercise 02 of the AoC 2024 challenge.

    Args:
        input_lines: An iterable of strings containing the input data.
    """

    input_lines: "Iterable[str]"

    def solve_part_1(self) -> int:
        """Solve the first part of the exercise.

        Returns:
            The result of the first part of the exercise.
        """
        return sum(
            is_safe_report(report_numbers)
            for report_numbers in self.parsed_input_line()
        )

    def solve_part_2(self) -> int:
        """Solve the second part of the exercise.

        Returns:
            The result of the second part of the exercise.
        """
        return sum(
            is_safe_report_with_tolerance(report_numbers)
            for report_numbers in self.parsed_input_line()
        )

    def parsed_input_line(self) -> "Generator[list[int], Any]":
        """Parse the input lines into a generator of lists of integers.

        Yields:
            A list of integers.
        """
        for input_line in self.input_lines:
            yield [int(num_str) for num_str in input_line.strip().split()]


def is_safe_report_with_tolerance(report_numbers: list[int]) -> bool:
    """Check if a report is safe with a tolerance of one missing number.

    Args:
        report_numbers: A list of integers representing the report.

    Returns:
        True if the report is safe, False otherwise.
    """
    if is_safe_report(report_numbers):
        return True

    for index in range(len(report_numbers)):
        report_numbers_ = report_numbers.copy()
        report_numbers_.pop(index)
        if is_safe_report(report_numbers_):
            return True
    return False


def is_safe_report(report_numbers: list[int]) -> bool:
    """Check if a report is safe.

    Args:
        report_numbers: A list of integers representing the report.

    Returns:
        True if the report is safe, False otherwise.
    """
    direction = None
    for index in range(1, len(report_numbers)):
        diff = report_numbers[index] - report_numbers[index - 1]
        if diff == 0:
            return False

        if direction is None:
            direction = diff > 0

        if (diff > 0) != direction:
            return False

        if abs(diff) > MAX_DIFFERENCE_BETWEEN_REPORT_NUMBERS:
            return False
    return True


if __name__ == "__main__":
    import pathlib

    INPUT_FILE = pathlib.Path(".exercise_input/exercise_02.txt")
    with INPUT_FILE.open() as f:
        print(Exercise02(input_lines=f.readlines()).solve_part_1())  # noqa: T201 # Might later be replaced with a proper CLI
        print(Exercise02(input_lines=f.readlines()).solve_part_2())  # noqa: T201
