class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        maxL, maxR = height[left], height[right]
        res = 0
        while left < right:
            if maxL <= maxR:
                left += 1
                elevation = maxL - height[left]
                res += elevation if elevation > 0 else 0
                maxL = max(maxL, height[left]) 
            else:
                right -= 1
                elevation = maxR - height[right]
                res += elevation if elevation > 0 else 0
                maxR = max(maxR, height[right])
        return res