class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                index = i

        return index + 1
        
