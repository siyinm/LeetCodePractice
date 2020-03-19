Given a *m* x *n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

### Solution

动态规划，在63/62基础上变化，每一步选择```dp[i][j] = min(dp[i - 1][j],dp[i][j - 1])+grid[i][j];```为到当前格子的最小路径

最后返回右下角那格的值就是最小路径

