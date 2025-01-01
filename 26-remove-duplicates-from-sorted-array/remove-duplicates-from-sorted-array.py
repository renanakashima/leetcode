class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1,len(nums)):
            i -= count
            print(i)
            if nums[i-1] == nums[i]:
                nums.pop(i-1)
                nums.append(1000)
                count += 1


        print(len(nums))
        print(nums)
        print(count)

        return len(nums)-count