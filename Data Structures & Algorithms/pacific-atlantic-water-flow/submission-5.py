class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, visit, prevHeights):
            if ((r, c) in visit or
                r < 0 or r >= rows or
                c < 0 or c >= columns or
                heights[r][c] < prevHeights):
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        for col in range(columns):
            dfs(0, col, pac, -1)
            dfs(rows - 1, col, atl, -1)

        for row in range(rows):
            dfs(row, 0, pac, -1)
            dfs(row, columns - 1, atl, -1)
        
        res = []
        for row in range(rows):
            for col in range(columns):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row, col])

        return res
            