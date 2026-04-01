class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store full word at terminal node


class Solution:
    def findWords(self, board, words):
        # ---------- build Trie ----------
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w

        ROWS, COLS = len(board), len(board[0])
        res = []
        dirs = ((-1,0), (1,0), (0,-1), (0,1))  # adjacent directions

        # ---------- DFS ----------
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return

            nxt = node.children[ch]

            # found a word
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None   # avoid duplicates

            board[r][c] = "#"  # mark visited

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)

            board[r][c] = ch  # restore

            # pruning: remove leaf node
            if not nxt.children:
                node.children.pop(ch)

        # ---------- start DFS ----------
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root)

        return res
