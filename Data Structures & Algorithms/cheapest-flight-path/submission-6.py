class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for s, d, c in flights:
            graph[s].append((d, c))
        
        minHeap = [(0, -1, src)]

        visited = {}

        while minHeap:
            cost, stops, node = heapq.heappop(minHeap)

            if node in visited and cost <= visited[node]:
                continue
            
            visited[node] = cost

            if stops > k:
                continue
                
            if node == dst:
                return cost
            
            for nei, c in graph[node]:
                heapq.heappush(minHeap, (cost + c, stops + 1, nei))
        
        return -1
            