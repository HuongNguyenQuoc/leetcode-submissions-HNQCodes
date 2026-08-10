class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}
        path = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            
            best = 1
            for dr, dc in path:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            dp[(r, c)] = best
            return best
        
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        
        return res