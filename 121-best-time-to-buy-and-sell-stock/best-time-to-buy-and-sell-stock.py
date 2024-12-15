class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        mn = prices[0]
        mn_index = 0
        mx = prices[0]
        mx_index = 0
        prof = 0

        # for i in range(0,len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j] - prices[i] > prof:
        #             mx_index = j
        #             mn_index = i
        #             prof = prices[j] - prices[i]
        #             print(j)
        #             print(i)
                
        
        # return prices[mx_index] - prices[mn_index]

        for i in range(1,len(prices)):
            if mn > prices[i]:
                mn = prices[i]
                mn_index = i
            if prices[i] - mn > prof:
                mx_index = i
                prof = prices[i] - mn

        #     if mx < prices[i]:
        #         mx = prices[i]
        #         mx_index = i

        # if mn_index < mx_index:
        #     prof = prices[mx_index] - prices[mn_index]
        return prof
    

        

        