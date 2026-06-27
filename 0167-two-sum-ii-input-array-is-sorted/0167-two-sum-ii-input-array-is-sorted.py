class Solution(object):
    def twoSum(self, numbers, target):
        n=len(numbers)
        d={}
        for i in range(n):
            rem=target-numbers[i]
            if rem in d:
                return [d[rem]+1,i+1]
            else:
                d[numbers[i]]=i
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        