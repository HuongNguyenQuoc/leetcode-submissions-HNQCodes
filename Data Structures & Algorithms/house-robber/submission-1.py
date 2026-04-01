class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        d = [-1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                d[i] = nums[i]
                continue
            elif i == 1:
                d[i] = max(d[i - 1], nums[i] + 0)
                continue
            d[i] = max(d[i - 1], nums[i] + d[i - 2])
        return d[i]