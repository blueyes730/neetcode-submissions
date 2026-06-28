class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        while l < len(prices):
            print(f"curr l: {prices[l]}")
            r = (l+1)
            while r < len(prices) and prices[r] > prices[l]:
                print(f"curr r: {prices[r]}")
                curr_profit = prices[r] - prices[l]
                print(f"curr_profit: {curr_profit}")
                max_profit = max(curr_profit, max_profit)
                print(f"max_profit: {max_profit}")
                r += 1
            l += 1
        return max_profit
                

        