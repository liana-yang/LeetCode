class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
        	return 0
        INT_MAX = 2147483647
        maxPro = 0 # And maxPro is the maximum profit we can get from day 0 to day i.
        minPrice = INT_MAX # minPrice is the minimum price from day 0 to day i.
        for i in range(len(prices)):
        	minPrice = min(minPrice, prices[i])
        	# How to get maxPro? Just get the larger one between current maxPro and prices[i] - minPrice.
        	maxPro = max(maxPro, prices[i] - minPrice)
        return maxPro
