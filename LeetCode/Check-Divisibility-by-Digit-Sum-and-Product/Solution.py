1class Solution(object):
2    def checkDivisibility(self, n):
3        t=n
4        sm=0
5        pd=1
6        while(t!=0):
7            r=t%10
8            sm=sm+r
9            pd=pd*r
10            t=t/10
11        if n%(sm+pd)==0:
12            return True
13        else:
14            return False
15
16        """
17        :type n: int
18        :rtype: bool
19        """
20        