class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if abs(total_sum) < target:
            return 0
        
        dp = {0: 1}

        for num in nums:
            next_dp = {}
            for total, count in dp.items():
                plus = total + num
                minus = total - num

                next_dp[plus] = next_dp.get(plus, 0) + count
                next_dp[minus] = next_dp.get(minus, 0) + count
            
            dp = next_dp
        
        return dp.get(target, 0)