def _merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(values: list[int]) -> list[int]:
    length = len(values)

    if length == 1:
        return values

    left = merge_sort(values[: length // 2])
    right = merge_sort(values[length // 2 :])

    return _merge(left, right)


input = [5, 2, 4, 6, 1, 3]
output = [1, 2, 3, 4, 5, 6]

result = merge_sort(input)

assert result == output, result
