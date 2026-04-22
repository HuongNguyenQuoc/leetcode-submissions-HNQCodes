class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) #Number of edge
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x]) #path compression
            return parent[x]
        
        def union(a: int, b: int) -> bool:
            root_a, root_b = find(a), find(b)

            if root_a == root_b:
                return False #cycle detected
            
            #union by size
            if size[root_a] < size[root_b]:
                parent[root_a] = root_b
                size[root_b] += size[root_a]
            else:
                parent[root_b] = root_a
                size[root_b] += size[root_a]

            return True    
        
        for u, v in edges:
            if not union(u, v): #cycle detected
                return [u, v]



            

            