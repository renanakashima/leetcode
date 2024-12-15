class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        mn = prices[0]
        prof = 0

        for i in range(1,len(prices)):
            if mn > prices[i]:
                mn = prices[i]
            if prices[i] - mn > prof:
                prof = prices[i] - mn

        return prof
    

        

        