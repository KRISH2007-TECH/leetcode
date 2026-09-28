1class Solution(object):
2    def smallestNumber(self, n, t):
3        p=1
4        s=n
5        while(s!=0):
6            sn=s%10
7            p=p*sn
8            s=s/10
9        while(p%t!=0):
10            n=n+1
11            p=1
12            s=n
13            while(s!=0):
14                sn=s%10
15                p=p*sn
16                s=s/10
17        return n 
18        
19
20
21
22
23
24        """
25        :type n: int
26        :type t: int
27        :rtype: int
28        """
29        