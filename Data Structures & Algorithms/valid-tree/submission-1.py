class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = {_:[] for _ in range(n)}
        for k, v in edges:
            dic[k].append(v)
        
        visit = set()
        def dfs(root):
            if root in visit:
                return False
            if not dic[root]:
                return True
            visit.add(root)
            for cur in dic[root]:
                if not dfs(cur):
                    return False
            return True
    
        for pre in dic:
            return dfs(pre)