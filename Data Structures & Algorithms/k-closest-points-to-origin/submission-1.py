class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for a, b in points: #O(n)
            m = a ** 2 + b ** 2
            minHeap.append((math.sqrt(m), a, b))
        heapq.heapify(minHeap) #O(n)
        res = []
        while k > 0:
            target, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res

        