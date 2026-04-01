class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return 0;
        unordered_map<char, int> mp;
        for(char i : s){
            mp[i]++;
        }
        for(auto c : t){
            if(mp.find(c) == mp.end() || mp[c] == 0){
                return 0;
            }
            mp[c]--;
        }
        return 1;  
    }
};
