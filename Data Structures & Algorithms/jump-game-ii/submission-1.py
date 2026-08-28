class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        memo = {}

        def dfs(i: int) -> int:
            if i >= n-1:
                return 0
            
            if i in memo:
                return memo[i]
            
            res = float("inf")
            for j in range(min(i+nums[i], n-1), i, -1):
                res = min(res, 1 + dfs(j))
            
            memo[i] = res
            return res
            
        return dfs(0)