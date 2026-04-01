class Solution:
    def isValid(self, s: str) -> bool:
        '''
        dic = {')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != dic[c]:
                        return False
        return not stack
'''






        hashMap = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in hashMap:
                if not stack:
                    return False
                else:
                    value = stack.pop()
                    if value != hashMap[c]:
                        return False
            else:
                stack.append(c)
        return not stack