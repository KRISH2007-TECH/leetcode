class Solution(object):
    def isAnagram(self, s, t):
        l=list(s)
        k=list(t)
        l.sort()
        k.sort()
        s=''.join(l)
        t=''.join(k)
        if t==s:
            return True
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        