class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        heap = [(0, k)]
        visited = set()
        res = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)
            res = max(res, time)

            for nei, w in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + w, nei))
        
        return res if len(visited) == n else -1