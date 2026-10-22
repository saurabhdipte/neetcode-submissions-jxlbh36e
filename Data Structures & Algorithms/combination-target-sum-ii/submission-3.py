class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        candidates.sort()
        def backtrack(i,cursum):
            if cursum==target:
                res.append(sol[:])
                return
            if i==len(candidates) or cursum>target:
                return 
            sol.append(candidates[i])
            backtrack(i+1,cursum+candidates[i])
            sol.pop()
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1,cursum)

        backtrack(0,0)
        return res
            

            