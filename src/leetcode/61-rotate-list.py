# 61. Rotate List

# Given the head of a linked list, rotate the list to the right by k places.


# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# 1->2->3->4->5
# 5->1->2->3->4 Rotate 1
# 4->5->1->2->3 Rotate 2

# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# 0->1->2
# 2->0->1 Rotate 1
# 1->2->0 Rotate 2
# 0->1->2 Rotate 3
# 2->0->1 Rotate 4


# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def rotate_linked_list(values: list[int], k: int) -> list[int]:
    if len(values) == k:
        return values

    if len(values) < k:
        k -= len(values)

    traversals = len(values) - (k % len(values))

    root = LinkedList(values.pop(0))
    current = root
    while values:
        current.next = LinkedList(values.pop(0))
        current = current.next

    current.next = root

    current = root
    for _ in range(1, traversals):
        current = current.next

    root = current.next
    current.next = None

    current = root
    values = []
    while current.next is not None:
        values.append(current.value)
        current = current.next

    values.append(current.value)
    return values


# Test Cases:
# Case 1:
inputs = [1, 2, 3, 4, 5]
k = 2
expected_result = [4, 5, 1, 2, 3]

result = rotate_linked_list(inputs, k)

assert result == expected_result, result

# Case 2:
inputs = [0, 1, 2]
k = 4
expected_result = [2, 0, 1]

result = rotate_linked_list(inputs, k)

assert result == expected_result, result
