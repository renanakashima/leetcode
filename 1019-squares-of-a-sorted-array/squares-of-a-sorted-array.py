class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sq = []
        for i in range(0,len(nums)):
            sq.append(0)
            sq[i] = nums[i] ** 2
        
        sq.sort()

        return sq