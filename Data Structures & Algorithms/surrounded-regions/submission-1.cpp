class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();

        auto bfs = [&](int row, int col) {
            queue<pair<int, int>> q;
            q.push({row, col});
            board[row][col] = '#';
            vector<pair<int, int>> v = {
                {-1, 0}, {1, 0}, {0, -1}, {0, 1}
            };

            while(!q.empty()) {
                auto& [r, c] = q.front();
                q.pop();
                for (auto& [dr, dc] : v) {
                    int nr = dr + r;
                    int nc = dc + c;
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && board[nr][nc] == 'O') {
                        board[nr][nc] = '#';
                        q.push({nr, nc});
                    }
                }
            }
        };

        // Check first and last column
        for (int i = 0; i < m; ++i) {
            if (board[i][0] == 'O') bfs(i, 0);
            if (board[i][n - 1] == 'O') bfs(i, n - 1);
        }

        // Check first and last row
        for (int i = 0; i < n; ++i) {
            if (board[0][i] == 'O') bfs(0, i);
            if (board[m - 1][i] == 'O') bfs(m - 1, i);
        }

        // Flip trapped '#' -> 'O', 'O' -> 'X'
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == '#') board[i][j] = 'O';
                else if (board[i][j] = 'O') board[i][j] = 'X';
            }
        } 
    }
};
