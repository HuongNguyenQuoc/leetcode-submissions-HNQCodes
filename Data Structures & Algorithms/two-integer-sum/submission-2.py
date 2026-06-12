class Solution:
    def binary(self, a, l, r, x):
        while l <= r:
            m = (l + r) // 2
            if a[m] == x:
                return m
            elif a[m] < x:
                l = m + 1
            else: r = m - 1
        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            pos = self.binary(nums, i + 1, len(nums) - 1, target - nums[i])
            if pos != -1:
                return [i, pos]
        return []
        


        