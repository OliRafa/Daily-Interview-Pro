# Hi, here's your problem today.

# You are only allowed to perform 2 operations, multiply a number by 2, or subtract a
# number by 1.
# Given a number x and a number y, find the minimum number of operations needed to go
# from x to y.

# Here's an example and some starter code.


# NAIVE APPROACH:
def min_operations(x, y):
    value = x
    operations = 0
    while value != y:
        if y % value:
            value -= 1
        else:
            value *= 2

        operations += 1

    return operations


# Test cases:
# Test 1:

# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
expected_result = 3
result = min_operations(6, 20)

assert result == expected_result, result

# Test 2:
# expected_result = 4
# result = min_operations(2, 5)

# assert result == expected_result, result
# Stuck in infinite loop

import queue

# Breadth First Algorithm
from copy import deepcopy

# A node of BFS traversal


class node:
    def __init__(self, val, level):
        self.val = val
        self.level = level


# Returns minimum number of operations
# needed to convert x into y using BFS


def minOperations(x, y):

    # To keep track of visited numbers
    # in BFS.
    visit = set()

    # Create a queue and enqueue x into it.
    q = queue.Queue()
    n = node(x, 0)
    q.put(n)

    # Do BFS starting from x
    while not q.empty():

        # Remove an item from queue
        t = q.get()

        # If the removed item is target
        # number y, return its level
        if t.val == y:
            return t.level

        # Mark dequeued number as visited
        visit.add(t.val)

        # If we can reach y in one more step
        if t.val * 2 == y or t.val - 1 == y:
            return t.level + 1

        n = deepcopy(t)
        # Insert children of t if not visited
        # already
        if t.val * 2 not in visit:
            n.val *= 2
            n.level += 1
            q.put(n)

        n = deepcopy(t)
        if t.val - 1 >= 0 and t.val - 1 not in visit:
            n.val -= 1
            n.level += 1
            q.put(n)


# Test cases:
# Test 1:

# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
expected_result = 3
result = minOperations(6, 20)

assert result == expected_result, result

# Test 2:
expected_result = 4
result = minOperations(2, 5)

assert result == expected_result, result
