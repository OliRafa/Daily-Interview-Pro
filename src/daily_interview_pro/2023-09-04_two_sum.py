# Hi, here's your problem today.

# You are given a list of numbers, and a target number k.
# Return whether or not there are two numbers in the list that add up to k.

# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


# O(n^2)
def two_sum_brute_force(numbers, k):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == k:
                return True

    return False


# O(n log n):
def two_sum_sorted_pointers(numbers, k):
    numbers = sorted(numbers)

    i = 0
    j = len(numbers) - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if sum == k:
            return True

        if sum > k:
            j += 1

        else:
            i += 1

    return False


# O(n)
def two_sum_complements(numbers, k):
    complements = []

    for number in numbers:
        if number in complements:
            return True

        complements.append(k - number)

    return False


two_sum = two_sum_complements

# Test Cases:
# Case 1:
inputs = [[4, 7, 1, -3, 2], 5]
expected_result = True

result = two_sum(*inputs)

assert result == expected_result, result

# Case 2:
inputs = [[2, 7, 11, 15], 9]
expected_result = True

result = two_sum(*inputs)

assert result == expected_result, result

# Case 3:
inputs = [[3, 2, 4], 6]
expected_result = True

result = two_sum(*inputs)

assert result == expected_result, result

# Case 4:
inputs = [[3, 3], 6]
expected_result = True

result = two_sum(*inputs)

assert result == expected_result, result
