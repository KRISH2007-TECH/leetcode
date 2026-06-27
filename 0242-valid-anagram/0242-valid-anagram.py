class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in t:
            if j not in d:
                return False
            else :
                d[j]-=1
        for i in d.values():
            if i!=0:
                return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        