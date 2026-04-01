class Solution {
public:
    const unordered_map<char, string> mapDigits = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };

    vector<string> res;

    void backtrack(const string &digits, int index, string &cur) {
        if (index == digits.length()) {
            res.push_back(cur);
            return;
        }

        string letters = mapDigits.at(digits[index]);

        for (const char &c : letters) {
            cur.push_back(c);
            backtrack(digits, index + 1, cur);
            cur.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        res.clear();
        string cur = "";
        backtrack(digits, 0, cur);
        return res;    
    }
};
/* TimeCP: O(n * 4^n) in worst case
SpaceCP: O(n) not include ouput; O(n) because space for depth recursion is length of input 'digits'
*/
