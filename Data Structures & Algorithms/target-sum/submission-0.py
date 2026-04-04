class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        ops=0
        def dfs(i,sum):
            nonlocal ops
            if i==len(nums):
                if sum==target:
                    ops+=1
                return
            sum+=nums[i]
            dfs(i+1,sum)
            sum-=nums[i]
            sum-=nums[i]
            dfs(i+1,sum)
        dfs(0,0)
        return ops