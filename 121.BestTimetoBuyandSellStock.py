class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentProfit, maxProfit, i, j = 0, 0, 0, 1
        
        while j < len(prices):
            if prices[i] < prices[j]:
                currentProfit = prices[j] - prices[i]
                maxProfit = max(maxProfit, currentProfit)
            else:
                i = j
            j += 1
        
        return maxProfit