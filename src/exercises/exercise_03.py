import re
from typing import TYPE_CHECKING, Any

import attrs

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable

REGEX_MUL = r"(?P<mul>mul\(\d{1,3},\d{1,3}\))"
REGEX_DO = r"(?P<do>do\(\))"
REGEX_DONT = r"(?P<dont>don’t\(\))"  # noqa: RUF001 # This character appears in the real input
COMBINED_PATTERN = re.compile(f"{REGEX_MUL}|{REGEX_DO}|{REGEX_DONT}")


@attrs.define
class Exercise03:
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
        concatenated_string = "".join(self.parsed_input_line())

        return sum(
            mul_string_to_result(re_match)
            for re_match in re.findall(REGEX_MUL, concatenated_string)
        )

    def solve_part_2(self) -> int:
        """Solve the second part of the exercise.

        Returns:
            The result of the first part of the exercise.

        Raises:
            ValueError: If the regex match is not one of the expected groups.
        """
        sum_of_multiplications = 0
        multiplications_enabled = True
        concatenated_string = "".join(self.parsed_input_line())

        for re_match in re.finditer(COMBINED_PATTERN, concatenated_string):
            match re_match.lastgroup:
                case "dont":
                    multiplications_enabled = False
                case "do":
                    multiplications_enabled = True
                case "mul":
                    if multiplications_enabled:
                        sum_of_multiplications += mul_string_to_result(
                            re_match.group(1)
                        )
                case _:
                    raise ValueError
        return sum_of_multiplications

    def parsed_input_line(self) -> "Generator[str, Any]":
        """Parse the input lines and yield the results.

        Yields:
            The parsed input line.
        """
        for input_line in self.input_lines:
            yield input_line.strip()


def mul_string_to_result(mul_string: str) -> int:
    """Convert the Mul(a,b) string to the result of the multiplication.

    Args:
        mul_string: The string containing the multiplication in the format Mul(a,b).

    Returns:
        The result of the multiplication
    """
    num_a, num_b = mul_string[4:-1].split(",")
    return int(num_a) * int(num_b)


if __name__ == "__main__":
    import pathlib

    INPUT_FILE = pathlib.Path(".exercise_input/exercise_03.txt")
    with INPUT_FILE.open() as f:
        print(Exercise03(input_lines=f.readlines()).solve_part_1())  # noqa: T201 # Might later be replaced with a proper CLI
        print(Exercise03(input_lines=f.readlines()).solve_part_2())  # noqa: T201
