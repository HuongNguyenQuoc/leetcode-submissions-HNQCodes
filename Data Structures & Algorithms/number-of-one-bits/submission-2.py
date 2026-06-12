class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        strs = str(n)
        for i in range(len(strs)):
            if strs[i] == "1":
                count += 1
        return count