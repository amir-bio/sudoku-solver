import random
from main import Board, solve
from pprint import pprint

def generate_sudoku() -> Board:
    """Generates a valid sudoku board with a few empty cells to be solved.

    The generate is done by getting a solution to an empty board. The implementation
    for the solver has been adjusted to choose guesses randomly which this
    functionality depends on to ensure different boards are returned each time.

    Raises:
        Exception: If no solution is found raises an exception; this is never
        expected to happen however added to pass strict typechecking.

    Returns:
        Board: Returns a valid sudoku board with a few missing cells to be solved.
    """
    # can't multiply by 9 again (i.e. [[0]*9]*9) as that would copy the reference of the first
    # row for all of them, which mean any value in first row would be copied to
    # the rest
    empty_board = [[0] * 9 for _ in range(9)]
    solved_board = solve(empty_board)

    # this check is unnecessary in reality as we never expect a solution to not
    # be found for the empty board, it's just added to pass strict type checking
    if solved_board is None:
        raise Exception("No solution found")

    # number of cells to remove roughly controls the difficulty
    cells_to_remove_per_row = 5
    for i in range(9):
        for j in random.sample(range(9), cells_to_remove_per_row):
            solved_board[i][j] = 0

    return solved_board

pprint(generate_sudoku())
