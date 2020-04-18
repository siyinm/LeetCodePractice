class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N <= 1:
            return 0
        ans = 0
        prev = 0
        for i in range(1, N):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans

