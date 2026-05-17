class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for sta, end, pri in flights:
            graph[sta].append([end, pri])

        minHeap = [(0, -1, src)]

        visited_stops = {}

        while minHeap:
            money, stops, start = heapq.heappop(minHeap)

            if start in visited_stops and visited_stops[start] <= stops:
                continue

            visited_stops[start] = stops 

            if start == dst:
                return money

            if stops == k:
                continue

            for end, pri in graph[start]:
                heapq.heappush(minHeap, (money + pri, stops + 1, end))
        
        return -1