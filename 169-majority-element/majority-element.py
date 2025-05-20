class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if candidate == nums[i]:
                count += 1
            elif candidate != nums[i] and count == 0:
                candidate = nums[i]
            else:
                count -= 1
        
        return candidate