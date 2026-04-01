class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        visited = [0] * n

        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)
        
        def dfs(cur, parent):
            visited[cur] = 1
            
            for nei in graph[cur]:
                if nei == parent:
                    continue
                if visited[nei] == 0:
                    dfs(nei, cur)
        
        res = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i, -1)
                res += 1
        return res