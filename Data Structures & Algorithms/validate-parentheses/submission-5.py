class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c in hashMap:
                stack.append(c)
            else:
                if not stack:
                    return False
                value = stack.pop()
                if hashMap[value] != c:
                    return False
        return not stack