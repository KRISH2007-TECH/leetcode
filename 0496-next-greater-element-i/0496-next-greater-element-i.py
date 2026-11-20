class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        x=[]
        for i in range(len(nums1)):
            k=nums2.index(nums1[i])
            for j in range(k+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    x.append(nums2[j])
                    break
            else:
                x.append(-1)
        return x
    
