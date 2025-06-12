class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer approach
        # left, right = 0, 1
        # result  = 0

        # while right < len(prices):
        #     if prices[left] < prices[right]:
        #         profit = prices[right] - prices[left]
        #         result = max(result, profit)
        #     else:
        #         left = right
        #     right += 1

        # return result

        # DP approach
        result = 0
        bestBuy = prices[0] # track the lowest price seen so far
        for sell in prices:
            result = max(result, sell - bestBuy) # try selling today
            bestBuy = min(bestBuy, sell) # update minBuy if today's price is lower

        return result
        
