class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i == len(nums) - 1:
                return True
            elif nums[i] == 0:
                return False
            if dfs(i + nums[i]):
                return True
        return dfs(0)