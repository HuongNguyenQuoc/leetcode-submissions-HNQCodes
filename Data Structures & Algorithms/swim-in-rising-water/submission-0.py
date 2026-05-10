class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        minHeap = [(grid[0][0], 0, 0)]

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while True:
            time, row, col = heapq.heappop(minHeap)

            if row == n - 1 and col == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    next_time = max(time, grid[nr][nc])
                    heapq.heappush(minHeap, (next_time, nr, nc))
                    visited[nr][nc] = True

            