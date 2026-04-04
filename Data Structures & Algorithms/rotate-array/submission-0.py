class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        new=[0]*len(nums)
        k=k%n
        for i in range(len(nums)):
            new[(i+k)%n]=nums[i]
        nums[:]=new
