# Hi, here's your problem today.

# You are given two linked-lists representing two non-negative integers.
# The digits arestored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Here is the function signature as a starting point (in Python):


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        while l1 or c:
            try:
                result = l1.val + l2.val + c
                if result == 10:
                    carry_over = 1
                    result_list = ListNode(0)

                else:
                    result_list = ListNode(result)
                    carry_over = 0

                result_list.next = self.addTwoNumbers(l1.next, l2.next, carry_over)
                return result_list

            except AttributeError:
                return ListNode(c)

        return None


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8


# Test cases
def parse_result(solution: Solution) -> int:
    result = []
    while solution:
        result.append(solution.val)
        solution = solution.next

    return int("".join(map(str, result)))


expected_result = 708

solution = Solution().addTwoNumbers(l1, l2)

result = parse_result(solution)
assert result == expected_result

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

expected_result = 7001

solution = Solution().addTwoNumbers(l1, l2)

result = parse_result(solution)
assert result == expected_result
