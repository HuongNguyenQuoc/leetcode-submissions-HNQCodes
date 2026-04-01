class Solution:
    def trap(self, height: List[int]) -> int:
        #Di chuyển left hoặc right kiểm tra xem maxL, maxR cái nào nhỏ hơn
        #Tại sao phải di chuyển cái nhỏ hơn mà không phải cái lớn hơn?
        #Vì nếu ta di chuyển con trỏ có maxL (maxR) lớn hơn thì ta không biết chính xác vị trí của con trỏ nhỏ hơn đáng ra ở đâu (water thu được phụ thuộc vào min)
        if not height:
            return 0
        left, right = 0, len(height) - 1
        maxL, maxR = height[left], height[right]
        res = 0
        while left < right:
            if maxL <= maxR:
                left += 1
                if height[left] > maxL:
                    maxL = height[left]
                res += maxL - height[left]
            else:
                right -= 1
                if height[right] > maxR:
                    maxR = height[right]
                res += maxR - height[right]
        return res