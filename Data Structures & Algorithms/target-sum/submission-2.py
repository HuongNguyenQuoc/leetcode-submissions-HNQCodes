class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def backtrack(i, curr_sum):
            if i == len(nums):
                return 1 if curr_sum == target else 0
            
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]
            
            add = backtrack(i + 1, curr_sum + nums[i])
            minus = backtrack(i + 1, curr_sum - nums[i])
            cache[(i, curr_sum)] = add + minus
            return cache[(i, curr_sum)]

        return backtrack(0, 0)