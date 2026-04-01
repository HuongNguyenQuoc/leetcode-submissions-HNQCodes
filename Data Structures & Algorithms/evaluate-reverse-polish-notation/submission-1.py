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
            x = stack.pop()
            y = stack.pop()
            stack.append(oper[c](y, x))
        return stack[0]