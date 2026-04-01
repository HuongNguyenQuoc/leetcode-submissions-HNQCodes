class Solution:
    def isPalindrome(self, s: str) -> bool:
        fillted = ""
        for i in s:
            if i.isalnum():
                fillted += i.lower()
        return fillted == fillted[::-1]