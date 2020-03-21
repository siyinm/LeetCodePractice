class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]
        for i in range(n):
            dp[i%2] = dp[i%2] + dp[(i+1)%2]

        return dp[(n+1)%2]
