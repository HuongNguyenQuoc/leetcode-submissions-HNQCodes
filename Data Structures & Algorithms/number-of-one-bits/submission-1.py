class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for c in n:
            if c == "1":
                count += 1
        return count