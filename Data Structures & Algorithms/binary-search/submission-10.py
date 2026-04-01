class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        def binary_search(l : int, r : int) -> int:
            if l > r:
                return -1
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return binary_search(l, m - 1)
            else:
                return binary_search(m + 1, r)
                

        return binary_search(l, r)