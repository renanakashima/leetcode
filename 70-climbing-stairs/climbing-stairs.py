class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        x = 1
        y = 2

        if n == 1:
            return x
        elif n == 2:
            return y

        for i in range(3,n+1):
            a = x + y
            x = y
            y = a

        return a