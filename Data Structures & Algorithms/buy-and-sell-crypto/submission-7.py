class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_brought = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            #print(prices[i], min_brought, profit)
            if prices[i] - min_brought > profit:
                profit = prices[i] - min_brought
            min_brought = min(min_brought, prices[i])
        return profit