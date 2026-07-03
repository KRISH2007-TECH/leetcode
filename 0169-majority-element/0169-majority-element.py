class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        nums.sort()
        return nums[n/2]

        """
        :type nums: List[int]
        :rtype: int
        """
        