class Solution(object):
    def moveZeroes(self, nums):
        i=0
        j=0
        while(i<len(nums)):
            if nums[i]!=0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j+=1
            else:
                i+=1
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        