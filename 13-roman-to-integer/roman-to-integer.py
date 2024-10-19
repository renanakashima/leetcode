class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num = 0
        for i in range(len(s)):
            if(i + 1 < len(s)) and (dictionary[s[i]] < dictionary[s[i+1]]):
                num -= dictionary[s[i]]

            else:
                num += dictionary[s[i]]
        return num