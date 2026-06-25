class Solution(object):
    def removeDuplicates(self, nums):
        s=1
        for i in range(2,len(nums)):
            if nums[i]!= nums[s-1]:
                s=s+1
                nums[s]=nums[i]
        return s+1

        """
        :type nums: List[int]
        :rtype: int
        """
        