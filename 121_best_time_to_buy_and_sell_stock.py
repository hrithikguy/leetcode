class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) <= 1:
            return 0
        cur_min = prices[0]
        best_profit = 0
        
        for i in prices:
            best_profit = max(best_profit, i - cur_min)
            cur_min = min(cur_min, i)
                
        return best_profit
