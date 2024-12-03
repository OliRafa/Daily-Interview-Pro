# https://adventofcode.com/2024/day/1#part2
# --- Part Two ---
# Your analysis only confirmed what everyone feared: the two lists of location IDs are
# indeed very different.

# Or are they?

# The Historians can't agree on which group made the mistakes or how to read most of the
# Chief's handwriting, but in the commotion you notice an interesting detail: a lot of
# location IDs appear in both lists! Maybe the other numbers aren't location IDs at all
# but rather misinterpreted handwriting.

# This time, you'll need to figure out exactly how often each number from the left list
# appears in the right list. Calculate a total similarity score by adding up each number
# in the left list after multiplying it by the number of times that number appears in
# the right list.

# Here are the same example lists again:

# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# For these example lists, here is the process of finding the similarity score:

# The first number in the left list is 3. It appears in the right list three times, so
# the similarity score increases by 3 * 3 = 9.
# The second number in the left list is 4. It appears in the right list once, so the
# similarity score increases by 4 * 1 = 4.
# The third number in the left list is 2. It does not appear in the right list, so the
# similarity score does not increase (2 * 0 = 0).
# The fourth number, 1, also does not appear in the right list.
# The fifth number, 3, appears in the right list three times; the similarity score
# increases by 9.
# The last number, 3, appears in the right list three times; the similarity score again
# increases by 9.
# So, for these example lists, the similarity score at the end of this process is 31
# (9 + 4 + 0 + 0 + 9 + 9).

# Once again consider your left and right lists. What is their similarity score?
from advent_of_code_2024.day_01_historian_hysteria_part_01 import (
    INPUTS_FILE_PATH,
    clean_inputs,
    transform_distance_pairs,
)
from advent_of_code_2024.utils.files import read_inputs


def calculate_distances_count(distances: list[int]) -> dict[int, int]:
    # Possibly Python's internal implementation for sorting is not linear, so it would
    # be bad for the execution time and the idea of solving the problem linearly.
    distances = sorted(distances)

    distances_count = {}
    previous = 0
    count = 1
    for distance in distances:
        if not previous:
            previous = distance
            continue

        if distance == previous:
            count += 1

        else:
            distances_count[previous] = count
            count = 1
            previous = distance

    distances_count[distance] = count

    return distances_count


def calculate_similarity_score(
    left_distances: list[int], right_distances: list[int]
) -> int:
    right_distances = calculate_distances_count(right_distances)

    similarity = 0
    for distance in left_distances:
        try:
            similarity += distance * right_distances[distance]

        except KeyError:
            continue

    return similarity


# Arrange
inputs = (
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3",
)

expected_result = 31

# Act
inputs = clean_inputs(inputs)

left_distances, right_distances = transform_distance_pairs(inputs)
# Doing it in O(n)
result = calculate_similarity_score(left_distances, right_distances)

# Assert
assert result == expected_result


# Now based on the provided file
inputs = read_inputs(INPUTS_FILE_PATH)
inputs = clean_inputs(inputs)

left_distances, right_distances = transform_distance_pairs(inputs)
result = calculate_similarity_score(left_distances, right_distances)

print(result)
