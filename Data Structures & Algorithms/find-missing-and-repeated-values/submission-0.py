class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n

        s_expected = N * (N + 1) // 2
        sq_expected = N * (N + 1) * (2 * N + 1) // 6

        s_actual = 0
        sq_actual = 0

        for row in grid:
            for x in row:
                s_actual += x
                sq_actual += x * x

        diff = s_actual - s_expected              # a - b
        sq_diff = sq_actual - sq_expected         # a^2 - b^2

        sum_ab = sq_diff // diff                  # a + b

        a = (diff + sum_ab) // 2
        b = a - diff

        return [a, b]