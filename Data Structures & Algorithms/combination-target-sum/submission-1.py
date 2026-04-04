class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        def backtracking(i,total):
            if total==target:
                sol.append(res[:])
                return
            if total>target or i==len(candidates):
                return
            res.append(candidates[i])
            backtracking(i,total+candidates[i])
            res.pop()
            backtracking(i+1,total)
        backtracking(0,0)
        return sol