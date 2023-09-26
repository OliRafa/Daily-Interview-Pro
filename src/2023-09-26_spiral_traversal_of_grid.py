# Hi, here's your problem today.

# You are given a 2D array of integers.
# Print out the clockwise spiral traversal of the matrix.

# Example:

# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]

# The clockwise spiral traversal of this array is:

# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

# Here is a starting point:


def _pop_vertical_values(M: list[list[int]], is_last_column: bool = False) -> list[int]:
    vertical_values = []
    if is_last_column:
        for row in M:
            vertical_values.append(row.pop(-1))

    else:
        for row in M:
            vertical_values.append(row.pop(0))

    return vertical_values


def _calculate_flatten_matrix(M: list[list[int]]) -> list[int]:
    POSSIBLE_MOVES_SEQUENCE = [
        "horizontal",
        "vertical_down",
        "horizontal_reverse",
        "vertical_up",
    ]

    flatten_matrix = []

    while M:
        for move in POSSIBLE_MOVES_SEQUENCE:
            match move:
                case "horizontal":
                    flatten_matrix += M.pop(0)
                case "vertical_down":
                    flatten_matrix += list(_pop_vertical_values(M, is_last_column=True))
                case "horizontal_reverse":
                    flatten_matrix += M.pop(-1)[::-1]
                case "vertical_up":
                    flatten_matrix += list(_pop_vertical_values(M))[::-1]

    return flatten_matrix


def matrix_spiral_print(M):
    spiral_matrix = _calculate_flatten_matrix(M)
    print(spiral_matrix)


grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12

# Test Cases
# Test Case 1:
grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
expected_result = [
    1,
    2,
    3,
    4,
    5,
    10,
    15,
    20,
    19,
    18,
    17,
    16,
    11,
    6,
    7,
    8,
    9,
    14,
    13,
    12,
]

result = _calculate_flatten_matrix(grid)

assert result == expected_result
