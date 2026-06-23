class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, curr_sum):
            if i == len(nums):
                return 1 if curr_sum == target else 0
            
            return (backtrack(i + 1, nums[i] + curr_sum) +
                    backtrack(i + 1, curr_sum - nums[i]))
        return backtrack(0, 0)