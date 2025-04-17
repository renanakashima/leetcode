class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(1,n):
                if i < j and nums[i] == nums[j] and (i * j) % k == 0:
                    count+=1

        return count