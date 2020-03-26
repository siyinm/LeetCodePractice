class Solution {
    vector<vector<int>> res;
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int N = nums.size();
        vector<int> em;
        res.push_back(em);
        for (int i = 1; i<=N; i++){
            combine(nums, i);
        }
        return res;    
    }
    
    void combine(vector<int>& nums, int k) {
        vector<int> com;
        dfs(com, 0, nums, k);
    }

    void dfs(vector<int>& com, int curr, vector<int>&  nums, int k) {
        if (com.size() == k){
            res.push_back(com);
            return;
        }
        int N = nums.size();
        for (int i = curr; i < N; i++){
            com.push_back(nums[i]);
            dfs(com, i+1, nums, k);
            com.pop_back();
        }
        return;
    }
};
