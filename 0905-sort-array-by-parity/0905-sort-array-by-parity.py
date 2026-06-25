class Solution(object):
    def sortArrayByParity(self, nums):
        s=0
        for i in range (1,len(nums)):
            if nums[s]%2==0:
                s+=1
                i+=1
            elif nums[i]%2==0:
                t=nums[i]
                nums[i]=nums[s]
                nums[s]=t
                s+=1
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        