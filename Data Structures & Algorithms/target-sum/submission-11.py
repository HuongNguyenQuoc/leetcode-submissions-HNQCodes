class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums):
            return 0
        
        # dp = {0: 1} -> 0 : count
        dp = {0: 1}

        for num in nums:
            next_dp = {}
            for total, count in dp.items():
                next_dp[total + num] = next_dp.get(total + num, 0) + count
                next_dp[total - num] = next_dp.get(total - num, 0) + count
            dp = next_dp
        
        return dp.get(target, 0)

