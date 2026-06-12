class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {_:[] for _ in range(n)}

        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        return True