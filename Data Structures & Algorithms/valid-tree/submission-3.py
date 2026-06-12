class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = {_:[] for _ in range(n)}
        for k, v in edges:
            dic[k].append(v)
        
        visit = set()
        def dfs(root):
            if root in visit:
                return False
            visit.add(root)
            if not dic[root]:
                return True
            for cur in dic[root]:
                if not dfs(cur):
                    return False
            return True
    
        for pre in dic:
            if not dfs(pre):
                return False
        return True