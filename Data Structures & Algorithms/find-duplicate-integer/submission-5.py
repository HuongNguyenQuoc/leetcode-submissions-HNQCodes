class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        duplicate = 0
        while duplicate != slow:
            slow = nums[slow]
            duplicate = nums[duplicate]
            if slow == duplicate:
                return slow