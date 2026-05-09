class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        minHeap = [(0, 0)]

        visited = set()
        total_cost = 0

        #Prim's
        while len(visited) < n:
            cost, curr = heapq.heappop(minHeap)

            if curr in visited:
                continue
            
            visited.add(curr)
            total_cost += cost

            x1, y1 = points[curr]

            for next_point in range(n):
                if next_point not in visited:
                    x2, y2 = points[next_point]
                    cost = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (cost, next_point))
                
        return total_cost
