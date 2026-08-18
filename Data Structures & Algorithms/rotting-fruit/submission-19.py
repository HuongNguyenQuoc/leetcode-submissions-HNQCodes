class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        path = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        maps = [[False] * n for _ in range(m)]
        res = 0
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    maps[i][j] = True
                elif grid[i][j] == 1:
                    fresh += 1

        while q:
            if fresh == 0:
                return res
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in path:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < m and 0 <= nc < n and maps[nr][nc] == False and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        maps[nr][nc] = True
                        q.append((nr, nc))
            res += 1
                    
        return res if fresh == 0 else -1


