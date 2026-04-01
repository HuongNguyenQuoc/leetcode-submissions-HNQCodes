class Solution:
    def rob(self, nums: List[int]) -> int:
        p2 = 0 #d[i - 2]
        p1 = 0 #d[i - 1]
        for money in nums:
            cur = max(p1, money + p2)
            p2 = p1
            p1 = cur
        return p1