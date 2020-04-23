class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [1,5,10,25]
        # 注意dp的初始化，表示没有硬币情况下凑金额0-n分
        dp = [0] * (n+1)
        dp[0] = 1  # 没有硬币凑0分为1种方式
        for i in range(len(coins)):
            for j in range(coins[i], n+1):
                dp[j] += dp[j-coins[i]]
        return dp[-1] % 1000000007
