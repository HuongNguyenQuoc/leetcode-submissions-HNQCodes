class Solution:

    def countPalindrome(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[r] == s[l]:
            count += 1
            l -= 1
            r += 1
        return count

    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPalindrome(s, i, i)
            res += self.countPalindrome(s, i, i + 1)
        return res