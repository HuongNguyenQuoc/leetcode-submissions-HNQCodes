class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(l, r):
            if l > r:
                return float("-inf")

            curSum = leftSum = rightSum = 0
            m = (l + r) // 2
            for i in range(m - 1, l - 1, -1):
                curSum += nums[i]
                leftSum = max(leftSum, curSum)
            curSum = 0
            for i in range(m + 1, r + 1):
                curSum += nums[i]
                rightSum = max(rightSum, curSum)
            return max(dfs(l, m - 1), dfs(m + 1, r), leftSum + nums[m] + rightSum)
        return dfs(0, len(nums) - 1)