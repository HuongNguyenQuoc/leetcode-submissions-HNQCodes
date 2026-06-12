class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)):
            for j in range(i, len(nums) - 1):
                tich = nums[j] * nums[j + 1]
                
                if (tich > res):
                    res = tich
        
        return res
