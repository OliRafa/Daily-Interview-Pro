# Given a string with the initial condition of dominoes, where:

# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side


# Figure out the final position of the dominoes. If there are dominoes that get pushed
# on both ends, the force cancels out and that domino remains upright.

# Example:
# Input:  ..R...L..R.
# Output: ..RR.LL..RR
# Here is your starting point:


class Solution(object):
    def push_dominoes(self, dominoes: str) -> str:
        self.dominoes = list(dominoes)
        for i in range(len(dominoes)):
            match dominoes[i]:
                case "L":
                    if self._look_behind(i, 1) == ".":
                        if not self._look_behind(i, 2) == "R":
                            self.dominoes[i - 1] = "L"

                case "R":
                    if self._look_ahead(i, 1) == ".":
                        if not self._look_ahead(i, 2) == "L":
                            self.dominoes[i + 1] = "R"

                case _:
                    continue

        return "".join(self.dominoes)

    def _look_ahead(self, current_element: int, num_elements: int) -> str | None:
        try:
            return self.dominoes[current_element + num_elements]

        except IndexError:
            return None

    def _look_behind(self, current_element: int, num_elements: int) -> str | None:
        try:
            return self.dominoes[current_element - num_elements]

        except IndexError:
            return None


# Test cases
# Test case 1:
expected_result = "..RR.LL..RR"
result = Solution().push_dominoes("..R...L..R.")

assert result == expected_result

# Test case 2:
expected_result = "LL.RR.LLRR.L.."
result = Solution().push_dominoes(".L.R...LR..L..")

assert result == expected_result
