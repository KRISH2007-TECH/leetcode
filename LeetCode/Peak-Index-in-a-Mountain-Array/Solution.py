1class Solution(object):
2    def peakIndexInMountainArray(self, arr):
3        for i in range(0,len(arr)):
4            if arr[i]>arr[i+1]:
5                return i
6
7        
8        """
9        :type arr: List[int]
10        :rtype: int
11        """
12        