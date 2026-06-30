class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # bought = prices[0]
        # for curr in prices[1:]:
        #     profit = max(profit, curr - bought)
        #     bought = min(bought, curr)
        
        # return profit
        l = 0
        profit = 0

        while l < len(prices):
            r = l + 1
            while r < len(prices) and prices[r] >= prices[l]:
                profit = max(profit, prices[r] - prices[l])
                r += 1
            l = r
        return profit

            
            