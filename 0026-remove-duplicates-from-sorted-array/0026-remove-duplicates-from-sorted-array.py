class Solution(object):
    def removeDuplicates(self, nums):
        s=0
        for i in range(1,len(nums)):
            if nums[i]!= nums[s]:
                s=s+1
                nums[s]=nums[i]
        return s+1
    """
        :type nums: List[int]
        :rtype: int
     """
        