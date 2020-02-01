class Solution {
public:
    vector<string> generateParenthesis(int n) {
        if (!n) return {};
        vector<string> ans;
        dfs("", n,0,n,ans);
        return ans;   
    }
    void dfs(string now, int left, int right, int n, vector<string>& ans ){
        if (left==0 && right==0 ){
            ans.push_back(now);
        }
        if (left>0){
            dfs(now+"(", left-1, right+1, n, ans);
        }
        if (right>0){
            dfs(now+")", left, right-1, n, ans);
        }
    }
    
};
