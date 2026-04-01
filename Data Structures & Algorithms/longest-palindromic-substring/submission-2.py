class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        MC = [0] * n
        R, C = 0, 0
        for i in range(1, n - 1):
            mirror = 2 * C - i
            if i < R:
                MC[i] = min(R - i, MC[mirror])
            while T[i + 1 + MC[i]] == T[i - 1 - MC[i]]:
                MC[i] += 1
            if i + MC[i] > R:
                C = i
                R = i + MC[i]
        
        val, idx = 0, 0
        for i in range(1, n - 1):
            if MC[i]  > val:
                val = MC[i]
                idx = i
        
        start = (idx - val) // 2
        return s[start : start + val]