# Hi, here's your problem today.

# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


# Here is a starting point:
class Solution:
    def __init__(self) -> None:
        self.movements = 0
        self.operations = 0

    def moveZeros(self, nums):
        for i in range(len(nums) - 1):
            self.movements += 1
            if nums[i] == 0:
                self.operations += 1
                for j in range(i, len(nums)):
                    self.movements += 1
                    if nums[j] != 0:
                        self.operations += 2
                        nums[i], nums[j] = nums[j], 0
                        break

    def moveZerosRecursive(self, nums):
        array_size = len(nums)
        if array_size == 1:
            return

        if array_size > 2:
            left = nums[: array_size // 2]
            right = nums[array_size // 2 :]

            self.moveZerosRecursive(left)
            self.moveZerosRecursive(right)

        for i in range(array_size - 1):
            self.movements += 1
            if nums[i] == 0:
                self.operations += 1
                for j in range(i, array_size):
                    self.movements += 1
                    if nums[j] != 0:
                        self.operations += 2
                        nums[i], nums[j] = nums[j], 0
                        break

    def moveZerosOptimized(self, nums):
        j = 0
        for i, element in enumerate(nums):
            self.movements += 1
            if element != 0:
                self.operations += 1
                if i != j:
                    self.operations += 2
                    nums[i], nums[j] = nums[j], nums[i]

                j += 1


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

# Test cases
# Test case 1:
vector = [0, 1, 0, 3, 12]
expected_result = [1, 3, 12, 0, 0]

solution = Solution()
solution.moveZeros(vector)

assert vector == expected_result
print(f"Movements: {solution.movements}")
print(f"Operations: {solution.operations}")

vector = [0, 1, 0, 3, 12]

solution = Solution()
solution.moveZerosRecursive(vector)

assert vector == expected_result
print(f"Movements Recursive: {solution.movements}")
print(f"Operations Recursive: {solution.operations}")

vector = [0, 1, 0, 3, 12]

solution = Solution()
solution.moveZerosOptimized(vector)

assert vector == expected_result
print(f"Movements Optimized: {solution.movements}")
print(f"Operations Optimized: {solution.operations}")

# Test case 2:
vector = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
expected_result = [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

solution = Solution()
solution.moveZeros(vector)

assert vector == expected_result

print(f"Movements: {solution.movements}")
print(f"Operations: {solution.operations}")

vector = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]

solution = Solution()
solution.moveZerosRecursive(vector)

assert vector == expected_result

print(f"Movements Recursive: {solution.movements}")
print(f"Operations Recursive: {solution.operations}")

vector = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]

solution = Solution()
solution.moveZerosOptimized(vector)

assert vector == expected_result

print(f"Movements Optimized: {solution.movements}")
print(f"Operations Optimized: {solution.operations}")

# Test case 3:
vector = [4, 8, 0, 0, 2, 0, 1, 0]
expected_result = [4, 8, 2, 1, 0, 0, 0, 0]

solution = Solution()
solution.moveZeros(vector)

assert vector == expected_result

print(f"Movements: {solution.movements}")
print(f"Operations: {solution.operations}")

vector = [4, 8, 0, 0, 2, 0, 1, 0]

solution = Solution()
solution.moveZerosRecursive(vector)

assert vector == expected_result

print(f"Movements Recursive: {solution.movements}")
print(f"Operations Recursive: {solution.operations}")

vector = [4, 8, 0, 0, 2, 0, 1, 0]

solution = Solution()
solution.moveZerosOptimized(vector)

assert vector == expected_result

print(f"Movements Optimized: {solution.movements}")
print(f"Operations Optimized: {solution.operations}")

# The optimized version has less operations when compared to the other two versions.
# It also has lower number of movements in comparison.
