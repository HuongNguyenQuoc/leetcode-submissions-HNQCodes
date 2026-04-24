class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)
        q = deque()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        for i in range(n + 1):
            if degree[i] == 1: #chỉ là lá thì sẽ cắt bớt dần
                q.append(i)
        
        while q:
            node = q.popleft()
            if degree[node] > 0:
                degree[node] -= 1
            
            for nei in adj[node]:
                if degree[nei] > 0:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)
        
        for u, v in reversed(edges):
            if degree[u] == 2 and degree[v] == 2:
                return [u, v]
            