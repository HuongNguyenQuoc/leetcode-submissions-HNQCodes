class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, i = [], 0
        while i < len(nums):
            left, right, cnt = 0, len(nums) - 1, 1
            if left != i and right != i:
                while left != i and right != i:
                    cnt *= nums[left] * nums[right]
                    left += 1
                    right -= 1
            if left != i and right == i:
                while left != i:
                    cnt *= nums[left]
                    left += 1
            if left == i and right != i:
                while right != i:
                    cnt *= nums[right]
                    right -= 1
            res.append(cnt)
            i += 1
        return res
            
