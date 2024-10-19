class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num = 0
        i = len(s) - 1
        while(i >= 0):
            num += dictionary[s[i]]
            if(s[i] == "V" or s[i] == "X") and i > 0:
                if(s[i-1] == "I"):
                    num -= 1
                    i -= 2
                else:
                    i -= 1
            elif(s[i] == "L" or s[i] == "C") and i > 0:
                if(s[i-1] == "X"):
                    num -= 10
                    i -= 2
                else:
                    i -= 1
            elif(s[i] == "D" or s[i] == "M") and i > 0:
                if(s[i-1] == "C"):
                    num -= 100
                    i -= 2
                else:
                    i -= 1
            elif(s[i] == "I") and i > 0:
                i -= 1
            else:
                break
        return num