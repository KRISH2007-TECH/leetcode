1class Solution(object):
2    def uniformArray(self, nums1):
3        odd=[]
4        even=[]
5        n=len(nums1)
6        i=0
7        if nums1[i]%2!=0:
8            while(i<n):
9                odd.append(nums1[i])
10                i+=1
11            if len(odd)==len(nums1):
12                return True
13            else:
14                return False
15        else:
16            while(i<n):
17                even.append(nums1[i])
18                i+=1
19            if len(even)==len(nums1):
20                return True
21            else:
22                return False
23        """
24        :type nums1: List[int]
25        :rtype: bool
26        """
27        