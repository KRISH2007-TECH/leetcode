class Solution(object):
    def twoSum(self, nums, target):
        i=0
        j=1
        while(i!=len(nums)):
            if nums[i]+nums[j]==target and i!=j:
                return [i,j]
                j=j+1
            else:
                j+=1
                if j==len(nums)-1:
                    i+=1
                    j=0

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        