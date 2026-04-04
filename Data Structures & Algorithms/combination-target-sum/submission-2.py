class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        def backtrack(i,curr):
            if curr==target:
                res.append(sol[:])
                return
            if curr>target or i==len(nums):
                return
            backtrack(i+1,curr)
            sol.append(nums[i])
            backtrack(i,curr+nums[i])
            sol.pop()            

        backtrack(0,0)
        return res