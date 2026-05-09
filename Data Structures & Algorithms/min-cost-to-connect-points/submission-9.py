class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_dist = [float("inf")] * n
        visited = [False] * n

        min_dist[0] = 0
        total_cost = 0

        for _ in range(n):
            curr = -1
            currCost = float("inf")

            for i in range(n):
                if not visited[i] and min_dist[i] < currCost:
                    currCost = min_dist[i] 
                    curr = i

            visited[curr] = True
            total_cost += currCost

            x1, y1 = points[curr]

            #Update distances for unvisited points
            for i in range(n):
                if not visited[i]:
                    x2, y2 = points[i]
                    cost = abs(x1 - x2) + abs(y1 - y2)
                    min_dist[i] = min(min_dist[i], cost)
        
        return total_cost


            
            

            