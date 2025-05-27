# 994. Rotting Oranges
# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
# https://assets.leetcode.com/uploads/2019/02/16/oranges.png
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.


from collections import deque


def oranges_rotting(grid) -> int:
    rows = len(grid)
    if rows == 0:
        return -1

    cols = len(grid[0])

    fresh_count = 0

    rotten = deque()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                rotten.append((i, j))
            elif grid[i][j] == 1:
                fresh_count += 1

    minutes = 0

    while rotten and fresh_count > 0:
        minutes += 1
        for _ in range(len(rotten)):
            x, y = rotten.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xx = x + dx
                yy = y + dy

                if xx < 0 or xx == rows or yy < 0 or yy == cols:
                    continue

                if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                    continue

                fresh_count -= 1

                grid[xx][yy] = 2

                rotten.append((xx, yy))

    return minutes if fresh_count == 0 else -1


input = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
output = 4
result = oranges_rotting(input)
assert result == output, result
