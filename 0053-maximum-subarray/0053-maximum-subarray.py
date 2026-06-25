class Solution(object):
    def maxSubArray(self, nums):
        c=0
        mx=nums[0]
        for i in range (0,len(nums)):
            c=c+nums[i]
            if c>mx:
                mx=c
            if c<0:
                c=0
        return mx
        """
        :type nums: List[int]
        :rtype: int
        """
        