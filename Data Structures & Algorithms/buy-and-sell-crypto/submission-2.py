class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = prices[0]
        for curr in prices[1:]:
            profit = max(profit, curr - bought)
            bought = min(bought, curr)
        
        return profit
        