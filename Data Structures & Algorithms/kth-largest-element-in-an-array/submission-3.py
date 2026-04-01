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
        def partition(t: int, p: int) -> int:
            i = t + 1
            j = p
            while i <= j:
                while i <= j and nums[i] <= nums[t]:
                    i += 1
                while i <= j and nums[j] >= nums[t]:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[t], nums[j] = nums[j], nums[t]
            return j
        
        l, r = 0, len(nums) - 1
        while True:
            pivot = partition(l, r)
            if pivot == len(nums) - k:
                return nums[pivot]
            elif pivot < len(nums) - k:
                l = pivot + 1
            else:
                r = pivot - 1