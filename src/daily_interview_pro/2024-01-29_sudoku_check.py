# Hi, here's your problem today.

# A Sudoku board is a 9x9 grid, where each row, column and each 3x3 subbox contains the
# number from 1-9.
# Here's an example of a Sudoku board.
# -------------
# |534|678|912|
# |672|195|348|
# |198|342|567|
# |------------
# |859|761|423|
# |426|853|791|
# |713|924|856|
# |------------
# |961|537|284|
# |287|419|635|
# |345|286|179|
# |------------

# Given a 9x9 board, determine if it is a valid Sudoku board.
# The board may be partially filled, where an empty cell will be represented by the
# space character ' '.

# Here's an example and some starting code:


# O(n^2)
def validate_sudoku_brute_force(board):
    for line in board:
        filtered_line = list(filter(lambda x: not x == " ", line))
        if len(filtered_line) != len(set(filtered_line)):
            return False

    for column in range(len(board)):
        column = [row[column] for row in board]
        filtered_column = list(filter(lambda x: not x == " ", column))
        if len(filtered_column) != len(set(filtered_column)):
            return False

    for i in range(0, len(board) - 1, 3):
        for j in range(0, len(board) - 1, 3):
            sub_box = (
                board[i][j : j + 3] + board[i + 1][j : j + 3] + board[i + 2][j : j + 3]
            )
            filtered_sub_box = list(filter(lambda x: not x == " ", sub_box))
            if len(filtered_sub_box) != len(set(filtered_sub_box)):
                return False

    return True


from collections import defaultdict


# O(n)
def validate_sudoku_optimal(board):
    rows = defaultdict(set)
    columns = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            current = board[r][c]
            if current == " ":
                continue

            if (
                current in rows[r]
                or current in columns[c]
                or current in boxes[(r // 3, c // 3)]
            ):
                return False

            rows[r].add(current)
            columns[c].add(current)
            boxes[r // 3, c // 3].add(current)

    return True


validate_sudoku = validate_sudoku_optimal

# Test Cases:
# Case 1:
board = [
    [5, " ", 4, 6, 7, 8, 9, 1, 2],
    [6, " ", 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]
expected_result = True

result = validate_sudoku(board)
assert result == expected_result, result

# Case 2: Repetition in Line
board = [
    [5, 5, 4, 6, 7, 8, 9, 1, 2],
    [6, " ", 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]
expected_result = False

result = validate_sudoku(board)
assert result == expected_result, result

# Case 2: Repetition in Column
board = [
    [8, 3, " ", " ", 7, " ", " ", " ", " "],
    [6, " ", " ", 1, 9, 5, " ", " ", " "],
    [" ", 9, " ", " ", " ", " ", " ", 6, " "],
    [8, " ", " ", " ", 6, " ", " ", " ", 3],
    [4, " ", " ", 8, " ", 3, " ", " ", 1],
    [7, " ", " ", " ", 2, " ", " ", " ", 6],
    [" ", 6, " ", " ", " ", " ", 2, 8, " "],
    [" ", " ", " ", 4, 1, 9, " ", " ", 5],
    [" ", " ", " ", " ", 8, " ", " ", 7, 9],
]
expected_result = False

result = validate_sudoku(board)
assert result == expected_result, result

# Case 2: Repetition in Sub-Box
board = [
    [5, 3, " ", " ", 7, " ", " ", " ", " "],
    [6, " ", " ", 1, 9, 5, " ", " ", " "],
    [" ", 9, 8, " ", " ", " ", " ", 6, " "],
    [8, " ", " ", " ", 6, " ", " ", " ", 3],
    [4, " ", " ", 8, " ", 3, " ", " ", 1],
    [7, " ", " ", " ", 2, " ", " ", " ", 6],
    [" ", 6, " ", " ", " ", " ", 2, 8, " "],
    [" ", " ", " ", 4, 1, 9, " ", " ", 5],
    [" ", " ", " ", " ", " ", " ", 8, 7, 9],
]

expected_result = False

result = validate_sudoku(board)
assert result == expected_result, result
