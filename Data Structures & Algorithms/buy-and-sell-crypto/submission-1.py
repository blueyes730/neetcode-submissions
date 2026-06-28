class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = 0
        # max_profit = 0
        # while l < len(prices):
        #     r = (l+1)
        #     while r < len(prices) and prices[r] > prices[l]:
        #         curr_profit = prices[r] - prices[l]
        #         max_profit = max(curr_profit, max_profit)
        #         r += 1
        #     l += 1
        # return max_profit

        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
                

        