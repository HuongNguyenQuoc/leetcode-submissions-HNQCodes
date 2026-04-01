class Solution:
    def countSubstrings(self, s: str) -> int:
        T = "^#" + "#".join(s) + "#$"
        C = R = 0
        P = [0] * len(T)
        for i in range(1, len(T) - 1):
            mirror = 2 * C - i
            if i < R:
                P[i] = min(R - i, P[mirror])
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C = i
                R = i + P[i]
        
        return sum((k + 1) // 2 for k in P)