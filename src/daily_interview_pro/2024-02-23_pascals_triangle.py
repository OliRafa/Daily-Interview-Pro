# Hi, here's your problem today.
#
# Pascal's Triangle is a triangle where all numbers are the sum of the two numbers above
# it.
# Here's an example of the Pascal's Triangle of size 5.
#
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
#
# Given an integer n, generate the n-th row of the Pascal's Triangle.
#
# Here's an example and some starter code.


def pascal_triangle_row(n):
    triangle = [[0 for _ in range(n)] for _ in range(n)]

    if n == 1:
        triangle[0][0] = 1
    for line in range(n):
        triangle[line][0] = 1

    for i in range(1, n):
        for j in range(1, n - 1):
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle[i][j] = value
            j += 1

        triangle[i][i] = 1

    return triangle[n - 1]


# Test cases
# Test case 1:
expected_result = [1]
result = pascal_triangle_row(1)
assert result == expected_result, result

# Test case 2:
expected_result = [1, 1]
result = pascal_triangle_row(2)
assert result == expected_result, result

# Test case 3:
expected_result = [1, 2, 1]
result = pascal_triangle_row(3)

assert result == expected_result, result

# Test case 4:
expected_result = [1, 3, 3, 1]
result = pascal_triangle_row(4)

assert result == expected_result, result

# Test case 5:
expected_result = [1, 4, 6, 4, 1]
result = pascal_triangle_row(5)

assert result == expected_result, result

# Test case 6:
expected_result = [1, 5, 10, 10, 5, 1]
result = pascal_triangle_row(6)

assert result == expected_result, result
