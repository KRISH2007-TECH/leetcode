class Solution(object):
    def maximumWealth(self, accounts):
        mx=0
        for i in accounts:
            mx= max(mx,sum(i))
        return mx
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        