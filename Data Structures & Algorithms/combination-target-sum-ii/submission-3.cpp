class Solution {
public:

    vector<vector<int>> res;
    vector<int> path;

    void backtrack(vector<int>& candidates, int target, int start) {
        if (target == 0) {  
            res.push_back(path);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            
            //Same level must not push_back into path
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }

            if (candidates[i] > target) {
                break;
            }

            path.push_back(candidates[i]);
            backtrack(candidates, target - candidates[i], i + 1);
            path.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        backtrack(candidates, target, 0);
        return res;
    }
};
