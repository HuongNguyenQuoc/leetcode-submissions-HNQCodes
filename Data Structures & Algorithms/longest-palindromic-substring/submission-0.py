class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r and resLen < j - i + 1:
                    res = s[i: j + 1]
                    resLen = j - i + 1
        
        return res