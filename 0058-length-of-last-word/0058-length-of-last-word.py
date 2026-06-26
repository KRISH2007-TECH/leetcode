class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        n=s
        count=0
        for i in range(len(n)-1,-1,-1):
            if s[i]!=' ':
                count=count+1
            else :
                break
        return count

    
    """
        :type s: str
        :rtype: int
        """
        