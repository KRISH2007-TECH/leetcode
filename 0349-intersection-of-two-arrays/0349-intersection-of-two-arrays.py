class Solution(object):
    def intersection(self, nums1, nums2):
        set1=set(nums1)
        set2=set(nums2)
        s=set1.intersection(set2)
        return list(s)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        