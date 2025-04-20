class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ""
        for i in range(len(digits)):
            string += str(digits[i])

        num = int(string)+1
        string = str(num)
        arr = []

        for j in range(len(string)):
            arr.append(int(string[j]))

        return arr