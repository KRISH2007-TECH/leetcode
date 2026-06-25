class Solution(object):
    def maxProfit(self, prices):
        mn=prices[0]
        p=0
        for i in range(1,len(prices)):
            cp=prices[i]-mn
            if cp>p:
                p=cp
            mn=min(mn,prices[i])
        return p
        """
        :type prices: List[int]
        :rtype: int
        """
        