class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for a, b in points: #O(n)
            heapq.heappush(minHeap, (a ** 2 + b ** 2, a, b))
        res = []
        for _ in range(k):
            target, a, b = heapq.heappop(minHeap)
            res.append([a, b])
        return res
        