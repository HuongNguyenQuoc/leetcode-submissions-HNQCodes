class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = (n * (n + 1)) // 2
        return target - sum(nums)
