class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(auto i : nums){
            mp[i]++;
            if (mp[i] >= 2) return 1;
        }
        return 0;
    }
};