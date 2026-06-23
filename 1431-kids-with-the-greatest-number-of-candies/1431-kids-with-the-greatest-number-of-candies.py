class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        l=max(candies)
        s=[]
        for i in candies:
            if i+extraCandies>=l:
                s.append(True)
            else:
                s.append(False)
        return s

        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        