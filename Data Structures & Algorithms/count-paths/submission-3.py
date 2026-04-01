class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = j = 1
        for i in range(m, m + n - 1):
            res *= i
            res //= j
            j += 1
        return res