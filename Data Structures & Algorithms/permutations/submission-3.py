class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,sol=[],[]
        def backtrack():
            if len(res)==len(nums):
                sol.append(res[:])
                return
            for i in range(len(nums)):
                # while i+1<len(nums) and nums[i]==nums[i+1]:
                #     i+=1
                if nums[i] not in res:
                    res.append(nums[i])
                    backtrack()
                    res.pop()
        backtrack()
        return sol