class Solution(object):
    def runningSum(self, nums):
        s=len(nums)
        i=0
        j=1
        while(j<s):
            nums[j]=nums[i]+nums[j]
            i=i+1
            j=j+1
        return nums


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        