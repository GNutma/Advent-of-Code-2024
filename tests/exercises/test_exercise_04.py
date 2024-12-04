from src.exercises import exercise_04


def test_part_1() -> None:
    """Test if the first part of the puzzle can be solved given the test input."""
    # GIVEN the following input
    input_data = [
        "MMMSXXMASM\n",
        "MSAMXMSMSA\n",
        "AMXSXMAAMM\n",
        "MSAMASMSMX\n",
        "XMASAMXAMM\n",
        "XXAMMXXAMA\n",
        "SMSMSASXSS\n",
        "SAXAMASAAA\n",
        "MAMMMXMMMM\n",
        "MXMXAXMASX\n",
    ]

    # AND it is used in as the input data
    solver = exercise_04.Exercise04(input_data)

    # WHEN the first part of the puzzle is solved
    result = solver.solve_part_1()

    # THEN the result should be as follows
    assert result == 18


def test_part_2() -> None:
    """Test if the second part of the puzzle can be solved given the test input."""
    # GIVEN the following input
    input_data = [
        "MMMSXXMASM\n",
        "MSAMXMSMSA\n",
        "AMXSXMAAMM\n",
        "MSAMASMSMX\n",
        "XMASAMXAMM\n",
        "XXAMMXXAMA\n",
        "SMSMSASXSS\n",
        "SAXAMASAAA\n",
        "MAMMMXMMMM\n",
        "MXMXAXMASX\n",
    ]
    # AND the inputted data is within the exercise solver
    solver = exercise_04.Exercise04(input_data)

    # WHEN the second part of the puzzle is solved
    result = solver.solve_part_2()

    # THEN the result should be as follows
    assert result == 9
