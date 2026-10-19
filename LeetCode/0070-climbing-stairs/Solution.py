class Solution(object):
    def climbStairs(self,n):
        if n <= 2:
            return n

        a, b = 1, 2   # ways for 1 step and 2 steps

        for i in range(3, n+1):
            c = a + b
            a = b
            b = c

        return b
