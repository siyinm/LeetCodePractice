class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid[0].size();
        int n = grid.size();
        vector<long> row(m, 0);
		vector<vector<long>> dp(n, row);   
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == 0 && j == 0) dp[i][j] = grid[i][j];
                else if (i == 0 ) dp[i][j] = dp[i][j-1]+grid[i][j];
                else if (j == 0 )  dp[i][j] = dp[i-1][j]+grid[i][j];
                else {
                    dp[i][j] = min(dp[i - 1][j],dp[i][j - 1])+grid[i][j];
                }
            }   
        }
        return dp[n - 1][m - 1];        
    }
};
