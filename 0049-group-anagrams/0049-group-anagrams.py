class Solution(object):
    def ss(self,s):
        s1=list(s)
        s1.sort()
        return "".join(s1)
    def groupAnagrams(self, strs):
        d={}
        for s in strs:
            key=self.ss(s)
            if key in d:
                d[key].append(s)
            else:
                d[key]=[s]
        return list(d.values())

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        