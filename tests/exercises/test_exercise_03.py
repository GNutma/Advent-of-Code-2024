from src.exercises import exercise_03


def test_part_1() -> None:
    """Test if the first part of the puzzle can be solved given the test input."""
    # GIVEN the following input
    input_data = [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))\n"
    ]

    # AND it is used in as the input data
    solver = exercise_03.Exercise03(input_data)

    # WHEN the first part of the puzzle is solved
    result = solver.solve_part_1()

    # THEN the result should be as follows
    assert result == 161


def test_part_2() -> None:
    """Test if the second part of the puzzle can be solved given the test input."""
    # GIVEN the following input
    input_data = [
        "xmul(2,4)&mul[3,7]!^don’t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))\n"  # noqa: RUF001 # This character appears in the real input
    ]
    # AND the inputted data is within the exercise solver
    solver = exercise_03.Exercise03(input_data)

    # WHEN the second part of the puzzle is solved
    result = solver.solve_part_2()

    # THEN the result should be as follows
    assert result == 48
