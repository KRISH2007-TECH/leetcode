class Solution(object):
    def subtractProductAndSum(self, n):
        x=n
        p=1
        s=0
        while(x>0):
            r=x%10
            s=s+r
            p=p*r
            x=x/10
        return(p-s)

        """
        :type n: int
        :rtype: int
        """
        