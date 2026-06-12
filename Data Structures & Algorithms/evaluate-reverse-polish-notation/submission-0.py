class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = {
            '+' : lambda a, b : a + b,
            '-' : lambda a, b : a - b,
            '*' : lambda a, b : a * b,
            '/' : lambda a, b : int(a / b)
        }

        for c in tokens:
            if c not in oper:
                stack.append(int(c))
                continue
            stack.append(oper[c](stack.pop(), stack.pop()))
        return stack[0]