class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        end = 0

        print(s.split())
        s = s.split()
        '''
        for i in range(1, len(s)+1):
            if s[-i] != " ":
                end = i
                break

        for i in range(end, len(s)+1):
            if s[-i] != " ":
                count += 1
            else:
                break
        '''
        return len(s[-1])