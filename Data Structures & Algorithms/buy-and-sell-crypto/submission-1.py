class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        length = len(prices) 
        maxP ,profit = 0,0
        while right < length:
            profit = prices[right] - prices[left]

            if (prices[left] < prices[right]):
                maxP = max(profit,maxP)
                print(f'if condition \n left: {left} right: {right} max: {maxP}')
            else:
                left = right
                print(f'else condition \n left: {left} right: {right}')

            right += 1

        return maxP