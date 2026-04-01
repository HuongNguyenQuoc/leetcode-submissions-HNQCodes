class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for (const int& x : nums) {
            s.insert(x);
        }
        return s.size() != nums.size();
    }
};