class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        for m in range(m,m+n):
            nums1[m] = nums2[index]
            index += 1

        nums1.sort()