# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
from functools import reduce


def _calculate_product(nums: list[int], k):
    if k == 0:
        filtered_nums = nums[1:]

    elif k == len(nums):
        filtered_nums = nums[:-1]

    else:
        filtered_nums = nums[:k] + nums[k + 1 :]

    return reduce(lambda x, y: x * y, filtered_nums)


def product_except_self(nums: list[int]) -> list[int]:
    products = []
    for i in range(len(nums)):
        products.append(_calculate_product(nums, i))

    return products


input = [1, 2, 3, 4]
output = [24, 12, 8, 6]
result = product_except_self(input)
assert result == output, result

input = [-1, 1, 0, -3, 3]
output = [0, 0, 9, 0, 0]
result = product_except_self(input)
assert result == output, result
