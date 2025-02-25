# Hi, here's your problem today.

# Given a string s and a character c, find the distance for all characters in the string
# to the character c in the string s.
# You can assume that the character c will appear at least once in the string.

# Here's an example and some starter code:


def shortest_dist(s, c):
    character_indexes = [i + 1 for i in range(len(s)) if s[i] == c]

    distances = []
    for i in range(len(s)):
        if s[i] == c:
            distances.append(0)
            continue

        distance = min(map(lambda x: abs(x - (i + 1)), character_indexes))
        distances.append(distance)

    return distances


# Test cases:
# Test 1:
expected_result = [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
result = shortest_dist("helloworld", "l")

assert result == expected_result, result
