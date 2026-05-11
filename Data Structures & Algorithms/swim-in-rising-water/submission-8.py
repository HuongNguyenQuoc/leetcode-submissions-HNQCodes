class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        heap = [(grid[0][0], 0, 0)]

        while True:
            time, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and
                    0 <= nc < n and
                    not visited[nr][nc]):

                    visited[nr][nc] = True
                    next_time = max(grid[nr][nc], time)
                    heapq.heappush(heap, (next_time, nr, nc))
                


