class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot=-1
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                pivot=i-1
                break
        if pivot==-1:
            nums.reverse()
            return
        swap=len(nums)-1
        while nums[pivot]>=nums[swap]:
            swap-=1
        nums[pivot],nums[swap]=nums[swap],nums[pivot]
        nums[pivot+1:len(nums)]=reversed(nums[pivot+1:len(nums)])
        return
