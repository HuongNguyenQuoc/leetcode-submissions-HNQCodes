class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        path = [[-1, 0], [1, 0], [0, -1],[0, 1]]
        res = 0
        rows, columns = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = '0'
            for dr, dc in path:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == '1':
                    dfs(nr, nc)
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res