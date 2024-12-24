class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 0 
        curr = 1 
        temp = 0 

        if n == 0:
            return 0

        for i in range(0, n-1):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr
        