class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1] and nums[i + 1] < nums[i + 2]:
                dp[i] = 1
        
        target = sum(dp)
        return target