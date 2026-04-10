class Solution {
public:
    
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int fresh = 0;
        int minutes = 0;
        queue<pair<int, int>> q;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == 2) q.push({row, col});
                else if (grid[row][col] == 1) fresh++;
            }
        }

        vector<pair<int, int>> directions = {
            {-1, 0}, {1, 0}, {0, -1}, {0, 1}
        };
        
        while (!q.empty()) {
            int length = q.size();
            bool status = false;
            for (int i = 0; i < length; i++) {
                auto [row, col] = q.front();
                q.pop();
                for (auto& [dr, dc] : directions) {
                    int nrow = dr + row;
                    int ncol = dc + col;
                    if (nrow < 0 || nrow == rows || ncol < 0 || ncol == cols) continue;
                    if (grid[nrow][ncol] == 1) {
                        status = true;
                        grid[nrow][ncol] = 2;
                        q.push({nrow, ncol});
                        fresh--;
                    }
                }
            }
            if (status) minutes++;
        }
        return fresh == 0 ? minutes : -1;
    }
};
