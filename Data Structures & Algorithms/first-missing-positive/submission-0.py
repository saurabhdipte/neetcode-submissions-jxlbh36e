class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        for index,num in enumerate(nums):
            if num<=0 or num>len(nums):
                nums[index]=1
        for index,num in enumerate(nums):
            index_to_change=abs(num)-1
            if nums[index_to_change]>0:
                nums[index_to_change]*=-1
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
        return len(nums)+1