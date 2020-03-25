class Solution {
vector<vector<int>> res;
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> com;
        dfs(com, 1, n, k);
        return res;
    }

    void dfs(vector<int>& com, int curr, int n, int k) {
        if (com.size() == k){
            res.push_back(com);
            return;
        }
        for (int i = curr; i <= n; i++){
            com.push_back(i);
            dfs(com, i+1, n, k);
            com.pop_back();
        }
        return;
    }
};
