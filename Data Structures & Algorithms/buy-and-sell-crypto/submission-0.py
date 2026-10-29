class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = 0
        for i in prices:
            minp = min(i, minp)
            maxp = max(i-minp, maxp)
        return maxp