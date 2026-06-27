class Solution(object):
    def isAnagram(self, s, t):
        
        if sorted(t)==sorted(s):
            return True
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        