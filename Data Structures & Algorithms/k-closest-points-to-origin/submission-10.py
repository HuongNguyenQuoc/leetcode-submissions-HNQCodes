class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''minHeap = []
        for a, b in points: #O(n)
            m = a ** 2 + b ** 2
            minHeap.append((math.sqrt(m), a, b))
        heapq.heapify(minHeap) #O(n)
        res = []
        while k > 0: #O(k)
            target, x, y = heapq.heappop(minHeap) #O(log(n))
            res.append([x, y])
            k -= 1
        return res
        #TimeCP: O(n + k*log(n))
    '''
        maxHeap = [] #Space: O(n)
        for a, b in points: #TimeCP: O(n)
            d = a ** 2 + b ** 2
            heapq.heappush(maxHeap, (-1 * d, a, b)) #O(logn)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap) #O(logn)

        return [[a, b] for value, a, b in maxHeap]  
        