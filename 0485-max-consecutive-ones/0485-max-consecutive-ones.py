class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        mx=0
        count=0
        for i in range (0,len(nums)):
            if nums[i]==1:
                count+=1
                if count>mx:
                    mx=count

            else :
                count=0
        return mx
        """
        :type nums: List[int]
        :rtype: int
        """
        