class Solution:
    def trap(self, height: List[int]) -> int:
        #Di chuyển left hoặc right kiểm tra xem maxL, maxR cái nào nhỏ hơn
        #Tại sao phải di chuyển cái nhỏ hơn mà không phải cái lớn hơn?
        #Vì nếu ta di chuyển con trỏ có maxL (maxR) lớn hơn thì ta không biết chính xác vị trí của con trỏ nhỏ hơn đáng ra ở đâu (water thu được phụ thuộc vào min)
        if not height:
            return 0
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res