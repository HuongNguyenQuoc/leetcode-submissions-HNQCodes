class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumCur, maxSum = 0, nums[0]
        for i in range(len(nums)):
            if sumCur < 0:
                sumCur = 0
            sumCur += nums[i]
            maxSum = max(maxSum, sumCur)
        return maxSum