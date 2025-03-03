# Hi, here's your problem today.

# You are given a string of parenthesis.
# Return the minimum number of parenthesis that would need to be removed in order to
# make the string valid.
# "Valid" means that each open parenthesis has a matching closed parenthesis.

# Example:

# "()())()"

# The following input should return 1.

# ")("

# Here's a start:


def count_invalid_parenthesis(string):
    counters = {"(": 0, ")": 0}

    for char in string:
        match char:
            case "(":
                counters["("] += 1

            case ")":
                counters[")"] += 1

    return abs(counters["("] - counters[")"])


# Test cases:
# Case 1:
input = "()())()"
expected_result = 1

result = count_invalid_parenthesis(input)

assert result == expected_result, result
