class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curMax, curMin = 1, 1

        for num in nums:
            target = num * curMax
            curMax = max(target, nums[i] * curMin, num)
            curMin = min(target, nums[i] * curMin, num)
            res = max(res, curMax)
        return res
            

        
