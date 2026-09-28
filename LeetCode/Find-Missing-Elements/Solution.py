1class Solution(object):
2    def findMissingElements(self, nums):
3        ans=[]
4        nums.sort()
5        n=nums[len(nums)-1]
6        for i in range(nums[0],n):
7            if i not in nums:
8                ans.append(i)
9        ans.sort()
10        return ans
11
12        """
13        :type nums: List[int]
14        :rtype: List[int]
15        """
16        