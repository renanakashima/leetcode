class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()
        tri = ""
        if nums[0] + nums[1] <= nums[2]:
            tri = "none"
        elif nums[0] == nums[2]:
            tri = "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            tri = "isosceles"
        else:
            tri = "scalene"
        return tri
