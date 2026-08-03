class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        mProfit = 0
        while r < len(prices):
            #profitable whenn
            if prices[r] > prices[l] :
                profit = prices[r] - prices[l]
                mProfit = max(profit, mProfit)
            else:
                l = r
            r += 1

 
        return mProfit
            