class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []

        for i, ch in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            else:
                if not len(left) and not len(star):
                    return False
                elif len(left):
                    left.pop()
                else:
                    star.pop()
        
        while len(left):
            if not len(star):
                return False
            a, b = left.pop(), star.pop()
            if a > b:
                return False
            
        return True