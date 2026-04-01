class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        path = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            for dr, dc in path:
                if dfs(r + dr, c + dc, i + 1):
                    return True
                
            board[r][c] = temp
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
