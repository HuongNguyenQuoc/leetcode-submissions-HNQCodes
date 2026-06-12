class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums.sort()
        curSum = 0
        maxSum = nums[i]
        for i in range(len(nums) - 1, -1, -1):
            curSum += nums[i]
            if curSum > maxSum:
                maxSum = curSum
                continue
            return maxSum