class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    min = float("inf")
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < min:
            self.minStack.append(val)
            self.min = val
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
