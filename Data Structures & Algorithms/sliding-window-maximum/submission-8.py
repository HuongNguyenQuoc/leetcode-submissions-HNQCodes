class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []

        for r in range(len(nums)):
            #remove giá trị cuối deque nhỏ hơn số hiện tại
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            #Thêm giá trị thỏa mãn vào queue
            q.append(r)
            #Di chuyển window
            if q[0] < r - k + 1:
                q.popleft()
            #Thêm giá trị đầu tiên trong queue vào list
            if r + 1 >= k:
                res.append(nums[q[0]])
        return res
        
            
