class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        m, n = len(A), len(B)
        total = m + n
        h = total // 2
        l, r = 0, m - 1
        while True:
            i = (l + r) // 2
            j = h - i - 2
            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i + 1] if i < m - 1 else float("inf")
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if j < n - 1 else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return min(A_right, B_right)
                k = max(A_left, B_left) +  min(A_right, B_right)
                return k / 2
            if A_left > B_right:
                r = i - 1
            else:
                l = i + 1