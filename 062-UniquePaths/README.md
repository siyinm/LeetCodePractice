A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

### Solution

1. 排列组合（类似高考题）

   机器人一定会走m+n-2步，即从m+n-2中挑出m-1步向下走$C_{m+n-2}^{m-1}$

2. dynamic programming

   我们令 `dp[i][j]` 是到达 `i, j` 最多路径

   动态方程：`dp[i][j] = dp[i-1][j] + dp[i][j-1]`

   注意，对于第一行 `dp[0][j]`，或者第一列 `dp[i][0]`，由于都是在边界，所以只能为 `1`

   时间复杂度：O(m∗n)*O*(*m*∗*n*)

   空间复杂度：O(m∗n)*O*(*m*∗*n*)

   优化：因为我们每次只需要 `dp[i-1][j],dp[i][j-1] `

   所以我们只要记录这两个数，可以简化到空间复杂度为O(n)（看代码）