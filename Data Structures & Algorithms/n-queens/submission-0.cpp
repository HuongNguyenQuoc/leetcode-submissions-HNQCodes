class Solution {
public:
    int n;
    vector<vector<string>> results;
    vector<string> board;
    vector<int> cols;
    vector<int> diag1; // row - col + (n - 1)
    vector<int> diag2; // row + col

    void backtrack(int row) {
        if (n == row) {
            results.push_back(board);
            return;
        }    

        for (int col = 0; col < n; col++) {
            int d1 = row - col + n - 1;
            int d2 = row + col;
            if (cols[col] && diag1[d1] && diag2[d2]) {
                //choose
                board[row][col] = 'Q';
                diag1[d1] = false;
                diag2[d2] = false;
                cols[col] = false;

                //explore
                backtrack(row + 1);

                //undo
                board[row][col] = '.';
                cols[col] = true;
                diag1[d1] = true;
                diag2[d2] = true;
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        this->n = n;
        board = vector<string>(n, string(n, '.'));
        cols = vector<int>(n, true);
        diag1 = vector<int>(2 * n - 1, true);
        diag2 = vector<int>(2 * n - 1, true);
        backtrack(0);
        return results;
    }
};

//TimeCP: O(n!)
/*
Nếu có board n * n thì tức là ta sẽ đi lần lượt từng hàng để đặt quân hậu. Vậy thì đi hàng đầu tiên thì sẽ có n cột khả năng đặt hậu. Then,
hàng thứ 2 sẽ còn (n - 1) cột khả năng đặt được, so on... -> n*(n-1)*(n-2)*...*1 = n!
*/
//SpaceCP: O(n) not include output vì đệ quy sâu nhất mới chỉ tốn O(n) -> tức là recusion theo row