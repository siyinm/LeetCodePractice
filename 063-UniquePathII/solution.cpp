class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid[0].size();
        int n = obstacleGrid.size();
        vector<long> row(m, 0);
		vector<vector<long>> dp(n, row);   
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (obstacleGrid[i][j] == 0){
                    if (i == 0 && j == 0) dp[i][j] = 1;
                    else if (i == 0 ) dp[i][j] = dp[i][j-1];
                    else if (j == 0 )  dp[i][j] = dp[i-1][j];
                    else {
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                    }
                }
                else {
                    dp[i][j] = 0;
                }
            }
        }
        return dp[n - 1][m - 1];        
    }
};
