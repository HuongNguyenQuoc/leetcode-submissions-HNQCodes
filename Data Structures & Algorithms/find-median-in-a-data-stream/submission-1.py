class MedianFinder:

    def __init__(self):
        self.large, self.small = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, -1 * num)

        if self.large and self.small and (-1 * self.large[0]) > self.small[0]:
            value = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, value)

        if len(self.large) > len(self.small) + 1:
            value = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, value)
        if len(self.small) > len(self.large) + 1:
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * value)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return -1 * self.large[0]
        if len(self.small) > len(self.large):
            return self.small[0]
        return (-1 * self.large[0] + self.small[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()