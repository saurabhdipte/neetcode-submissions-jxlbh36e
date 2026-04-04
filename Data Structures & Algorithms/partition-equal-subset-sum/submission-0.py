class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        total=sum(nums)
        half=total//2
        def backtrack(i,cursum):
            if cursum==half:
                return True
            if cursum>half or i==len(nums):
                return
            #suppose we take the current element
            if backtrack(i+1,cursum + nums[i]): return True
            #suppose we dont
            if backtrack(i+1,cursum):
                return True
            return False
            
        return backtrack(0,0)
