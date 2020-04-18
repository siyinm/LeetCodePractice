class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N <= 1:
            return 0
        dp = [0 for i in range(N)]
        prev = prices[0]
        for i in range(1, N):
            if prices[i] < prices[i-1]:
                prev = min(prices[i], prev)
                dp[i] = 0
            else:
                dp[i] = prices[i] - prev
        return max(dp)

