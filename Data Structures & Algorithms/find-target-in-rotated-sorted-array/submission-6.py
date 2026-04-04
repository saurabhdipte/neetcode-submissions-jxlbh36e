class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        pivot=l
        def binarysearch(left,right):
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return -1
        index = binarysearch(0,pivot-1)
        if index==-1:
            index=binarysearch(pivot,len(nums)-1)
        return index