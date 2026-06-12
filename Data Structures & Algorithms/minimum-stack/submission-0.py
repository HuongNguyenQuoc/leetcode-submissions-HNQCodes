class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        stack.append(val)
        min = float("-inf")
        if val > min:
            minStack.append(val)

    def pop(self) -> None:
        stack.pop()

    def top(self) -> int:
        return stack[-1]

    def getMin(self) -> int:
        return minStack[-1]
