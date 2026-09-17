1class Solution(object):
2    def singleNonDuplicate(self, nums):
3        i=0
4        j=len(nums)-1
5        while(i<j):
6            mid=(i+j)//2
7            if mid % 2 == 1:
8                mid -= 1
9            if nums[mid] == nums[mid + 1]:
10                i = mid + 2
11            else:
12                j = mid
13            
14        return nums[i]
15        """
16        :type nums: List[int]
17        :rtype: int
18        """
19        