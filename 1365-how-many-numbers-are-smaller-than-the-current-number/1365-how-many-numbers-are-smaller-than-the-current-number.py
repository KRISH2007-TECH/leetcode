class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l=[]
        for i in range(len(nums)) :
            count=0
            for j in range(len(nums)) :
                if nums[j]<nums[i]  :
                    count=count+1
            l.append(count)
        return l

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        