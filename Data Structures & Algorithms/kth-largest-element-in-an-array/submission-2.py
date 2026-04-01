class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        target = [-num for num in nums]
        heapq.heapify(target)
        while True:
            g = heapq.heappop(target)
            k -= 1
            if k == 0:
                return -g
        '''
        '''
        nums.sort()
        return nums[len(nums) - k]
        '''
        return heapq.nlargest(k, nums)[-1]