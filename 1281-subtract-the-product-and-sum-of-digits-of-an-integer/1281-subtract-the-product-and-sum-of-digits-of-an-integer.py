class Solution(object):
    def subtractProductAndSum(self, n):
        s=0
        p=1
        while(n>0):
            r=n%10
            s=s+r
            p=p*r
            n=n/10
        return (p-s)



        """
        :type n: int
        :rtype: int
        """
        