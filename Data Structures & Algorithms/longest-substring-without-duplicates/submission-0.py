class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestChar = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in longestChar:
                longestChar.remove(s[l])
                l += 1
            longestChar.add(s[r])
            res = max(res, r - l + 1)
        return res
        
