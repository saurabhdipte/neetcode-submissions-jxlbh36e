class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res={}

        def dfs(i,sum):

            if i==len(nums):
                if sum==target:
                    return 1
                return 0

            if (i,sum) in res:
                return res[(i,sum)]

            res[(i,sum)] = dfs(i+1,sum+nums[i]) + dfs(i+1,sum-nums[i])
            return res[(i,sum)]

        return dfs(0,0)
     

            


  
        