class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str = ""
        i = 0
        word = 0
        shortest = len(strs[0])

        for w in range(1,len(strs)):
            if(shortest > len(strs[w])):
                shortest = len(strs[w])
            else:
                w + 1

        while(word < len(strs) and i < shortest):
            if(shortest == 0):
                return str
            elif(len(strs) == 1):
                return strs[0]
            elif(word + 1 < len(strs) and strs[word][i] == strs[word+1][i]):
                if(word + 1 == len(strs)-1):
                    str += strs[word][i]
                    i += 1
                    word = 0
                else: 
                    word += 1
            else:
                return str
        return str        