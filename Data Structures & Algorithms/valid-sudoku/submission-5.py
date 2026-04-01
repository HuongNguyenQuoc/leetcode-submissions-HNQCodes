class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: defaultdict[int, set] = defaultdict(set)
        cols: defaultdict[int, set] = defaultdict(set)
        square:  defaultdict[set, set] = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in square[(r // 3, c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        return True