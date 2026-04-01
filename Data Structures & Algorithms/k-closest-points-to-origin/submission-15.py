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
        '''
        maxHeap = []
        for a, b in points: #Time: O(n)
            d = a ** 2 + b ** 2
            heapq.heappush(maxHeap, (-d, a, b)) #Time: O(logk)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap) #Time: O(logk)
        return [[a, b] for target, a, b in maxHeap]
        '''
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]
