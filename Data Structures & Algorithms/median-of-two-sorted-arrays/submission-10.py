class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if not A and not B:
            return -1
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        if m == 0:
            if n % 2 == 0:
                return (B[n // 2 - 1] + B[n // 2]) / 2
            else:
                return B[n // 2]
        total = m + n
        h = total // 2
        l, r = 0, m
        while True:
            i = (l + r) // 2
            j = h - i
            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < m else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < n else float("inf")
            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                return min(A_right, B_right)
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
