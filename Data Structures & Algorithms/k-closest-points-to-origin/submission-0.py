class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for a, b in points: #O(n)
            k = a ** 2 + b ** 2
            minHeap.append((sqrt(k), a, b))
        heapq.heapify(minHeap) #O(n)
        res = []
        while k > 0:
            target, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res

        