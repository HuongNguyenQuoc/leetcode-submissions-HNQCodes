class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for s, d, p in flights:
            graph[s].append((d, p))

        minHeap = [(0, -1, src)]
        visited = {}

        while minHeap:
            price, stops, node = heapq.heappop(minHeap)

            if node in visited and visited[node] <= stops:
                continue
            
            visited[node] = stops

            if node == dst:
                return price
            
            if stops == k:
                continue
            
            for nei, p in graph[node]:
                heapq.heappush(minHeap, (price + p, stops + 1, nei))
        
        return -1
