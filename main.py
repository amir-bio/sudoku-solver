from typing import List, Tuple, Union  # , Set, Dict, , Optional
from pprint import pprint
import random

Board = List[List[int]]


def solve(board: Board) -> Union[Board, None]:
    """Given a sudoku board (2d array of ints) will return a solution of the sudoku board.

    Args:
        board (Board): The unsolved sudoku board. A value of in any cell '0'
        indicates an unset cell.

    Returns:
        solved board (Board | None): A solution to the given solved board if
        there's one, otherwise returns None.
    """
    row, col = next_empty_cell(board)
    # row (and col) will be set to None if there's no next empty cell
    if row is None or col is None:
        return board

    # shuffle the list of numbers to guess instead of going incrementall from 1 to 9
    # The solution will still be valid, and this is utilised by the generater to
    # generate valid sudoku boards.
    for i in random.sample(range(1, 10), 9):
        if valid_value(board, row, col, i):
            board[row][col] = i

            solved_board = solve(board)
            if solved_board is None:
                board[row][col] = 0
            else:
                return solved_board

    return None


def valid_value(board: Board, row: int, col: int, value: int) -> bool:
    # check values in same row
    for i, v in enumerate(board[row]):
        if v == value and i != col:
            return False

    # check values in same column
    for i in range(len(board)):
        if board[i][col] == value and i != row:
            return False

    # check values in same 3x3 box
    box_start_x = (col//3) * 3
    box_start_y = (row//3) * 3
    for i in range(box_start_y, box_start_y + 3):
        for j in range(box_start_x, box_start_x + 3):
            if board[i][j] == value and (i, j) != (row, col):
                return False

    return True


positionOrNone = Union[int, None]


def next_empty_cell(board: Board) -> Tuple[positionOrNone, positionOrNone]:
    """Given a sudoku board, returns the row and col position of the next empty
    cell, where empty is defined as a cell with a value of 0.

    Args:
        board (Board): Sudoku board to return the next empty cell from/

    Returns:
        Tuple[positionOrNone, positionOrNone]: A tuple of positions; if there's
        no more empty cells, returns (None, None)
    """
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 0:
                return (i, j)
    return (None, None)


sample_unsolved_board = [
    [1, 0, 8, 0, 0, 0, 0, 5, 3],
    [7, 0, 2, 5, 0, 3, 0, 0, 0],
    [0, 0, 0, 8, 1, 0, 0, 2, 6],
    [0, 0, 7, 0, 8, 4, 2, 0, 0],
    [0, 1, 5, 0, 3, 2, 0, 0, 0],
    [4, 2, 6, 0, 5, 0, 0, 0, 0],
    [3, 0, 0, 2, 7, 0, 0, 6, 0],
    [2, 0, 0, 0, 0, 0, 4, 8, 7],
    [0, 0, 9, 0, 4, 8, 5, 0, 0]
]

# print("Unsolved board")
# pprint(sample_unsolved_board)

# print("\n\nSolved board")
# pprint(solve(sample_unsolved_board))
