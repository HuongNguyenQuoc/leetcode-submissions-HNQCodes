class Solution {
public:

    vector<string> res;

    void backtrack(string& current, int n, int open, int close) {
        if (current.length() == 2 * n) {
            res.push_back(current);
            return;
        }

        // Thêm dấu '('
        if (open < n) {
            current.push_back('(');
            backtrack(current, n, open + 1, close);
            current.pop_back();
        }   

        //Thêm dấu ')'
        if (close < open) {
            current.push_back(')');
            backtrack(current, n, open, close + 1);
            current.pop_back();
        }
    }

    vector<string> generateParenthesis(int n) {
        string current = "";
        backtrack(current, n, 0, 0);
        return res;
    }
};
