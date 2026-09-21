1class Solution(object):
2    def reverseString(self, s):
3        i=0
4        n=(len(s)/2)-1
5        j=len(s)-1
6        while(i<j):
7            temp=s[i]
8            s[i]=s[j]
9            s[j]=temp
10            i+=1
11            j-=1
12        """
13        :type s: List[str]
14        :rtype: None Do not return anything, modify s in-place instead.
15        """
16        