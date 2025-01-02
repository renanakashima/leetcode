class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            i -= count
            if nums[i] == val:
                nums.pop(i)
                nums.append(1000)
                count += 1

        return len(nums) - count

        

