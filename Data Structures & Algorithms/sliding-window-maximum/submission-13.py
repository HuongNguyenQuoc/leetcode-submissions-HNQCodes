class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = nums[0]
        rightMax[n - 1] = nums[n - 1]
        for i in range(1, n):
            if i % k == 0:
                leftMax[i] = nums[i]
            else:
                leftMax[i] = max(nums[i], leftMax[i - 1])

            x = n - i - 1
            if x % k == 0:
                rightMax[x] = nums[x]
            else:
                rightMax[x] = max(rightMax[x + 1], nums[x])
        
        res = [0] * (n - k + 1)
        for i in range(n - k + 1):
            res[i] = max(leftMax[i + k - 1], rightMax[i])
        return res

        
            
