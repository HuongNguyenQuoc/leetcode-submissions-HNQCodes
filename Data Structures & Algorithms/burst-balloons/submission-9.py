class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cache = dict()
        
        def dfs(nums):
            if len(nums) == 1:
                return nums[0]
            key = tuple(nums)
            if key in cache:
                return cache[key]
            
            result = 0
            for i in range(len(nums)):
                left = nums[i - 1] if i > 0 else 1
                mid = nums[i]
                right = nums[i + 1] if i < len(nums) - 1 else 1
                coins = left * mid * right
                result = max(result, dfs(nums[:i] + nums[i+1:]) + coins)

            cache[key] = result
            return result
        
        return dfs(nums)
