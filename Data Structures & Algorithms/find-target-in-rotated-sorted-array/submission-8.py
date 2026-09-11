class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>nums[right]:
                left = mid  + 1
            else:
                right=mid
        pivot=left
        def binarysearch(left,right):
            while left<=right:
                mid =left + (right-left)//2
                if nums[mid]>target:
                    
                    right = mid - 1
                elif nums[mid]<target:
                    left = mid+1
                else:
                    return mid
            return -1
        index = binarysearch(0,pivot-1)
        if index==-1:
            index=binarysearch(pivot,len(nums)-1)
        return index