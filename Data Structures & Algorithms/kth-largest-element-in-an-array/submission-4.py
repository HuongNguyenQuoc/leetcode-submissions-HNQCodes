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
        '''
        return heapq.nlargest(k, nums)[-1] #heapq.nlargest(k, nums): lấy k phần tử lớn nhất trong mảng rồi return 1 list sắp giảm dần; [-1]: tức là lấy từ cuối về (Phần tử nhỏ nhất trong k element)
        '''
        minHeap = []
        for num in nums: #O(n)
            heapq.heappush(minHeap, num) #O(logk)
            if len(minHeap) > k:
                heapq.heappop(minHeap) #O(logk)
        return minHeap[0]

        #Time: O(nlogk)
        #Space: O(k)
