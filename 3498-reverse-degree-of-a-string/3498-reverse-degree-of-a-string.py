class Solution(object):
    def reverseDegree(self, s):
        d={}
        for i in range(1,27):
            d[chr(96+i)]=27-i
        print(d)
        sm=0
        for i in range (len(s)):
            if s[i] in d:
                sm=sm+d[s[i]]*(i+1)
        return(sm)
    """
        :type s: str
        :rtype: int
    """
        