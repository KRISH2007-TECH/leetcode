class Solution(object):
    def findpow(self,x,n):
        if n==0:
            return (1)
        a=self.findpow(x,n//2)
        if n%2==0:
            return (a*a)
        else:
            return (a*a*x)
    def myPow(self, x, n):
        if n>=0:
            return self.findpow(x,n)
        else:
            return 1/self.findpow(x,n*(-1))

        
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        