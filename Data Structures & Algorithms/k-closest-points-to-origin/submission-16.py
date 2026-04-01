class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        minHeap = []
        for a, b in points: #Time: O(n)
            minHeap.append((a ** 2 + b ** 2, a, b))
        heapq.heapify(minHeap)
        res = []
        for _ in range(k): #Time: O(k)
            target, a, b = heapq.heappop(minHeap) #Time: O(logn)
            res.append([a, b])
        return res
        '''
        maxHeap = []
        for a, b in points: #Time: O(n)
            d = a ** 2 + b ** 2
            heapq.heappush(maxHeap, (-d, a, b)) #Time: O(logk)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap) #Time: O(logk)
        return [[a, b] for target, a, b in maxHeap]
        