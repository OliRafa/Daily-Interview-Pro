# Hi, here's your problem today.

# Given a list, find the k-th largest element in the list.
# Input: list = [3, 5, 2, 4, 6, 8], k = 3
# Output: 5
# Here is a starting point:


def findKthLargest(nums, k):
    return max(nums[:k])


print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5

# Test cases
expected_result = 5
vector = [3, 5, 2, 4, 6, 8]
k = 3

result = findKthLargest(vector, k)

assert result == expected_result
