class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr = set()
        digits.sort()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    num = digits[i]*100 + digits[j]*10 + digits[k]
                    if num % 2 == 0 and i!=j and j!=k and i!=k and num >= 100\
                    and num not in arr:
                        arr.add(num)
        lis = [item for item in arr]
        lis.sort()
        return lis