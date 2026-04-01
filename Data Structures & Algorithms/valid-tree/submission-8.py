class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = {_:[] for _ in range(n)}
        visit = set()
        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)
        
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visit) == n