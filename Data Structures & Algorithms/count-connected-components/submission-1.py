class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {_:[] for _ in range(n)}
        visited = [0] * n

        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)
        
        def dfs(cur, parent):
            if visited[cur] == 0:
                visited[cur] = 1
            
            for nei in graph[cur]:
                if nei == parent:
                    continue
                dfs(nei, cur)
        
        res = 0
        for _ in range(n):
            if visited[_] == 0:
                visited[_] = 1
                dfs(graph[_], _)
                res += 1
        return res