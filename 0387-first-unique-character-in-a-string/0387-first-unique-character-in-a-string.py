class Solution(object):
    def firstUniqChar(self, s):
        n=len(s)
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1    
        """
        :type s: str
        :rtype: int
        """
        