class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        mx=0
        count=0
        for i in nums:
            if i==1:
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
        