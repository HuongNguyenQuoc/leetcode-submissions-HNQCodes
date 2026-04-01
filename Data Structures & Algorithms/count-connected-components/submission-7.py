class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(u1):
            target = u1
            while target != par[target]:
                par[target] = par[par[target]]
                target = par[target]
            return target

        def union(u1, u2):
            p1, p2 = find(u1), find(u2)

            if p1 == p2:
                return 0
            else:
                if rank[p1] > rank[p2]:
                    par[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]
            return 1


        res = n
        for u1, u2 in edges:
            res -= union(u1, u2)
        
        return res
