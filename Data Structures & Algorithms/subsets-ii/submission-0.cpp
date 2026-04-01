class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;

    void backtrack(vector<int>& nums, int start) {
        res.push_back(path);

        for (int i = start; i < nums.size(); i++) {
            //Bỏ qua các giá trị bằng nhau tại cùng cấp độ
            if (i > start && nums[i] == nums[i -1]) {
                continue;
            }
            path.push_back(nums[i]);
            backtrack(nums, i + 1); //mở rộng
            path.pop_back();
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        backtrack(nums, 0);
        return res;
    }
};
