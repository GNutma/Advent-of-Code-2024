from src.exercises import exercise_02


def test_part_1() -> None:
    """Test if the first part of the puzzle can be solved given the test input."""
    # GIVEN the following input
    input_data = [
        "7 6 4 2 1\n",
        "1 2 7 8 9\n",
        "9 7 6 2 1\n",
        "1 3 2 4 5\n",
        "8 6 4 4 1\n",
        "1 3 6 7 9\n",
    ]
    # AND the inputted data is within the exercise
    solver = exercise_02.Exercise02(input_data)

    # WHEN
    result = solver.solve_part_1()

    assert result == 2


def test_part_2() -> None:
    """Test if the second part of the puzzle can be solved given the test input."""
    # GIVEN the following input
    input_data = [
        "7 6 4 2 1\n",
        "1 2 7 8 9\n",
        "9 7 6 2 1\n",
        "1 3 2 4 5\n",
        "8 6 4 4 1\n",
        "1 3 6 7 9\n",
    ]
    # AND the inputted data is within the exercise
    solver = exercise_02.Exercise02(input_data)

    # WHEN
    result = solver.solve_part_2()

    assert result == 4
