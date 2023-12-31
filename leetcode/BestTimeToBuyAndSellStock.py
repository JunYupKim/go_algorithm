class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
 
        min_price = 1e9
        max_price = 0 
        for i in range(len(prices)):
            min_price = min(min_price,prices[i]) 
            max_price = max(max_price, prices[i]-min_price )

        return max_price
            

            