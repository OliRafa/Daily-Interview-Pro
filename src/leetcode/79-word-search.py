# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15

# board and word consists of only lowercase and uppercase English letters.

# Follow up: Could you use search pruning to make your solution faster with a larger board?


def is_word_in_board(word, board):
    rows = len(board)
    columns = len(board[0])
    paths = set()

    def dfs(row_position, column_position, letter_position):
        if letter_position == len(word):
            return True

        if (
            row_position < 0
            or column_position < 0
            or row_position >= rows
            or column_position >= columns
            or board[row_position][column_position] != word[letter_position]
            or (row_position, column_position) in paths
        ):
            return False

        paths.add((row_position, column_position))
        res = (
            dfs(row_position + 1, column_position, letter_position + 1)
            or dfs(row_position - 1, column_position, letter_position + 1)
            or dfs(row_position, column_position + 1, letter_position + 1)
            or dfs(row_position, column_position - 1, letter_position + 1)
        )
        paths.remove((row_position, column_position))
        return res

    for i in range(rows):
        for j in range(columns):
            if dfs(i, j, 0):
                return True

    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
assert is_word_in_board(word, board) is True

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
assert is_word_in_board(word, board) is True

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
assert is_word_in_board(word, board) is False
