# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Example 4:

# Input: s = "([])"
# Output: true


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pairs = ("()", "[]", "{}")
        for char in s:
            if char in [")", "]", "}"]:
                if not stack:
                    return False

                previous_opening = stack.pop()
                if not f"{previous_opening}{char}" in valid_pairs:
                    return False

            else:
                stack.append(char)

        return True


# Test cases:
# Case 1:
input = "()"
excpected_result = True

result = Solution().isValid(input)

assert result == excpected_result, result

# Case 2:
input = "()[]{}"
excpected_result = True

result = Solution().isValid(input)

assert result == excpected_result, result

# Case 3:
input = "(]"
excpected_result = False

result = Solution().isValid(input)

assert result == excpected_result, result

# Case 4:
input = "([])"
excpected_result = True

result = Solution().isValid(input)

assert result == excpected_result, result

# Case 5:
input = ")("
excpected_result = False

result = Solution().isValid(input)

assert result == excpected_result, result

# Case 6:
input = "([)]"
excpected_result = False

result = Solution().isValid(input)

assert result == excpected_result, result
