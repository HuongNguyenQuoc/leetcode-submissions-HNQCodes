class Solution {
public:
    int rows;
    int cols;

    int dfs(vector<vector<int>>& grid, int row, int col) {
        //Ngoài vùng grid
        if (row < 0 || row >= rows || col < 0 || col >= cols) return 0;
        // Ô là nước
        if (grid[row][col] == 0) return 0;
        //Đánh dấu ô hiện tại đã được thăm
        grid[row][col] = 0;
        //Đếm số ô của 1 vùng island theo 4 hướng
        return 1 
            + dfs(grid, row - 1, col) 
            + dfs(grid, row + 1, col) 
            + dfs(grid, row, col - 1) 
            + dfs(grid, row, col + 1);
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        this->rows = grid.size();
        this->cols = grid[0].size();
        int maxArea = 0;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == 1) {
                    int area = dfs(grid, row, col);
                    maxArea = max(maxArea, area);
                }
            }
        }
        return maxArea;
    }
};

/*
TimeCP: O(n * m); n là số hàng và m là số cột vì phải duyệt qua từng ô trong grid
SpaceCP: O(n * m) in worst case bởi vì độ sâu đệ quy lớn nhất là 1 island lớn full 1
*/