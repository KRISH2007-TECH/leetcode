1class Solution(object):
2    def smallestIndex(self, nums):
3        mx=len(nums)
4        for i in range (len(nums)):
5            sm=0
6            t=nums[i]
7            while(t!=0):
8                r=t%10
9                sm=sm+r
10                t=t/10
11            if mx>sm and i==sm:
12                mx=sm
13                
14        if mx == len(nums):
15            return -1
16        else:
17            return mx
18
19
20
21        """
22        :type nums: List[int]
23        :rtype: int
24        """
25        