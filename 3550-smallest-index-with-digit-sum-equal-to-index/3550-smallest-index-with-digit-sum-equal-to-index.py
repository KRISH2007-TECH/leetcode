class Solution(object):
    def smallestIndex(self, nums):
        mx=len(nums)
        for i in range (len(nums)):
            sm=0
            t=nums[i]
            while(t!=0):
                r=t%10
                sm=sm+r
                t=t/10
            if mx>sm and i==sm:
                mx=sm
                
        if mx == len(nums):
            return -1
        else:
            return mx



        """
        :type nums: List[int]
        :rtype: int
        """
        