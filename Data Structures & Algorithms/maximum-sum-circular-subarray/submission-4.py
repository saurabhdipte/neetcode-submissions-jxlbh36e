class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:


        cursum=nums[0]
        minsum = nums[0]
        for i in range(1,len(nums)):
            cursum = min(cursum + nums[i],nums[i])
            minsum = min(cursum,minsum)
        total = sum(nums)
        total_min =  total - minsum

        cursum=nums[0]
        maxsum = nums[0]
        for i in range(1,len(nums)):
            cursum = max(cursum + nums[i],nums[i])
            maxsum = max(cursum,maxsum)
        
        if maxsum<0:
            return maxsum

        return max(maxsum,total_min)



