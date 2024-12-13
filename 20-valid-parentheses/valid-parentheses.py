class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        arr = []

        for i in range(0, len(s)):
            if (s[i] == ")" or s[i] == "]" or s[i] == "}") and len(arr) == 0:
                return False
            elif s[i] == "(" or s[i] == "[" or s[i] == "{" :
                arr.append(s[i])
            elif s[i] == ")":
                last = arr.pop()
                if last != "(":
                    return False
            elif s[i] == "}":
                last = arr.pop()
                if last != "{":
                    return False
            elif s[i] == "]":
                last = arr.pop()
                if last != "[":
                    return False

        if len(arr) == 0:
            return True
        else:
            return False