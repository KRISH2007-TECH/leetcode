class Solution(object):
    def maxProduct(self, nums):
        mx1=0
        mx2=0
        for i in nums:
            if i>mx1:
                mx2=mx1
                mx1=i
            elif i>mx2:
                mx2=i
        return((mx1-1)*(mx2-1))
        """
        :type nums: List[int]
        :rtype: int
        """
        