class Solution(object):
    def countDigits(self, num):
        t=num
        count=0
        while(t!=0):
            r=t%10
            if num%r==0:
                count=count+1
            t=t/10
        return count
        """
        :type num: int
        :rtype: int
        """
        