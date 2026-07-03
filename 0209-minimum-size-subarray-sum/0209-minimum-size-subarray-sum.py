class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        if ans == float('inf'):
            return 0

        return ans       
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        