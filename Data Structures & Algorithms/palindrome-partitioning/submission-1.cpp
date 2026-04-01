class Solution {
public:
    
    vector<vector<string>> res;
    vector<string> path;

    bool isPalindrome(int left, int right, const string& s) {
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    void backtrack(const string& s, int start) {
        if (start == s.size()) {
            res.push_back(path);
            return;
        }

        for (int end = start; end < s.size(); end++) {
            if (isPalindrome(start, end, s)) {
                path.push_back(s.substr(start, end - start + 1));
                backtrack(s, end + 1);
                path.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        backtrack(s, 0);
        return res;
    }
};
