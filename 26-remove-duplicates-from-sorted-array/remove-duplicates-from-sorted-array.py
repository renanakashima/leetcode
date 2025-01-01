class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1,len(nums)):
            i -= count
            if nums[i-1] == nums[i]:
                nums.pop(i-1)
                nums.append(1000)
                count += 1

        return len(nums)-count