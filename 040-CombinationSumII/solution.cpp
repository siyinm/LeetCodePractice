class Solution {
private:
    vector<vector<int>> ans;
    vector<int> vec;
    vector<int> candidates;
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        std::sort(candidates.begin(), candidates.end());
        this->candidates = candidates;
        dfs(0, target);
        return ans;
    }
    void dfs(int start, int target){
        if (target == 0){
            ans.push_back(vec);
            return;
        }
        for (int i =start; i<candidates.size() && target - candidates[i] >= 0; i++){
            if (i>start && candidates[i]==candidates[i-1]) continue;
            vec.push_back(candidates[i]);
            dfs(i+1, target-candidates[i] );
            vec.pop_back();
        }
    }
};
