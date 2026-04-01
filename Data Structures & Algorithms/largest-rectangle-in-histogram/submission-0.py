class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_num = 0
        for i, height in enumerate(heights):
            z = i #z represents the index that was just popped
            while stack and height < stack[-1][0]:
                a, b = stack.pop() #a : height, b : index
                w = i - b
                h = a
                area = h * w
                max_num = max(max_num, area)
                z = b
            stack.append((height, z))
        
        while stack:
            a, b = stack.pop()
            w = n - b
            h = a
            max_num = max(max_num, h * w)
        return max_num