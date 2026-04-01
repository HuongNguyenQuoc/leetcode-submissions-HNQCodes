class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)
        return res
            

        
