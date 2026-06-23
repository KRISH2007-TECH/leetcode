class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        t=x
        s=0
        while(t!=0):
            r=t%10
            s=s*10+r
            t=t/10
        if x==s:
            return True
        else :
            return False
        """
        :type x: int
        :rtype: bool
        """
        