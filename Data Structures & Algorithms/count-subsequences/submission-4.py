class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = {} #cache results to avoid redundant calculations

        def dfs(i: int, j: int) -> int:
            if j == n:
                return 1
            if i == m:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            #Continue incrementing i until it goes outside the array bounds
            result = dfs(i + 1, j)
            
            if s[i] == t[j]:
                result += dfs(i + 1, j + 1)
            
            memo[(i, j)] = result
            return result

        return dfs(0, 0)