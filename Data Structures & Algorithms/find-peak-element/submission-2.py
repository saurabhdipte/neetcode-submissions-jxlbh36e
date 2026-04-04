class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<nums[m-1] and m>0:
                r=m-1
            elif m<len(nums)-1 and nums[m] < nums[m+1] :
                l=m+1
            else:
                return m