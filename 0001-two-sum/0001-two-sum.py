class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        d={}
        for i in range (n):
            rem=target-nums[i]
            if rem in d:
                return [d[rem],i]
            else :
                d[nums[i]]=i
       
            

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        