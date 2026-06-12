class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for c in str(n):
            if c == "1":
                count += 1
        return count