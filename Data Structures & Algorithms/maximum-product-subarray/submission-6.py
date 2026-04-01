class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curMax, curMin = 1, 1

        for i in range(len(nums)):
            target = nums[i]
            curMax, curMin = max(nums[i]  * curMax, nums[i] * curMin, nums[i]), min(nums[i] * curMax, nums[i] * curMin, nums[i])
            res = max(res, curMax)
        return max(res, curMax)
            

        
