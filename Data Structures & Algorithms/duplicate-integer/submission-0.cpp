class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> mp;
        for(int i : nums){
            mp[i]++;
            if(mp[i] > 1) return 1;
        }
        return 0;
    }
};