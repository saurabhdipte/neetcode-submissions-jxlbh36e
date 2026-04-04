class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sol=[],[]
        n=len(nums)
        def backtrack(i):
            if i==n:
                res.append(sol[:])
                return
            
            #notpicking any number
            backtrack(i+1)

            #pickinga number
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res


        