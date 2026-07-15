class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_arr = [0]*len(prices)
        max_r = 0
        for i in range(len(prices)-1,-1,-1):
            max_r = max(max_r, prices[i])
            max_arr[i]=max_r
        #print(max_arr)
        profit = 0
        for i in range(0, len(prices)):
            if prices[i]<max_arr[i]:
                profit = max(profit, max_arr[i]-prices[i])
        return profit
        