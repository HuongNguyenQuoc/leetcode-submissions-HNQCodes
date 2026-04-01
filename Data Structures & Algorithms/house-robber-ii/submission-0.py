class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        
        def rob_linear(arr):
            p1, p2 = 0, 0 #p1:d[i - 1]; p2:d[i - 2]
            for money in arr:
                p2, p1 = p1, max(p1, money + p2)
            return p1
            
        return max(rob_linear(nums[:len(nums) - 1]), rob_linear(nums[1:]))