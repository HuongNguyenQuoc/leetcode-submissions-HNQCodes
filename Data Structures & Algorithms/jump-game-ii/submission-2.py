class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1): #Worse case will be: O(n)
                farthest = max(farthest, i + nums[i])
            l = r+1
            r = farthest
            res += 1
        
        return res
    
# The cost of time complexity: O(n)