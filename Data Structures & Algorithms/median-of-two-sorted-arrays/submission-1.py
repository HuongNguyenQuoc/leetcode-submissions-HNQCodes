class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        target = nums1 + nums2
        target.sort()
        n = len(target) - 1
        if n % 2 != 0:
            return (target[n // 2] + target[n // 2 + 1]) / 2
        else:
            return target[n // 2]