class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if abs(target) > total_sum:
            return 0
        
        dp = {0: 1}

        for num in nums:
            next_dp = {}
            for total, count in dp.items():
                add = total + num
                minus = total - num

                next_dp[add] = next_dp.get(add, 0) + count
                next_dp[minus] = next_dp.get(minus, 0) + count

            dp = next_dp
        
        return dp.get(target, 0)