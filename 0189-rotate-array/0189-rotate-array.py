class Solution(object):
    def rev(self,nums,l,r):
       
        while(l<r):
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
            l+=1
            r-=1
    def rotate(self, nums, k):
        n=len(nums)
        k%=n
        self.rev(nums,0,n-1)
        self.rev(nums,0,k-1)
        self.rev(nums,k,n-1)
        return nums
    
    

        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        