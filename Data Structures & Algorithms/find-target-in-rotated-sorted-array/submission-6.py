class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            if nums[l] <= nums[m]:
                if nums[m] < target or target < nums[l]: l = m + 1
                else: r = m - 1
            else:
                if target > nums[m] and target <= nums[r]: l = m + 1
                else: r = m - 1
        return -1 if l > r else m