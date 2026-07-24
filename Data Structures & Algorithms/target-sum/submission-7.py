class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def backtrack(index, current_sum):
            if (index, current_sum) in dp:
                return dp[(index, current_sum)]
            if index == n:
                return 1 if current_sum == target else 0

            add = backtrack(index + 1, current_sum + nums[index])
            subtract = backtrack(index + 1, current_sum - nums[index])
            result = add + subtract
            dp[(index, current_sum)] = result
            
            return dp[(index, current_sum)]

        return backtrack(0, 0)