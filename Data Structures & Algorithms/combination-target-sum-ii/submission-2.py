class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        candidates.sort()
        def backtrack(i,curr):
            if curr==target:
                sol.append(res[:])
                return
            if curr>target or i==len(candidates):
                return
            
            res.append(candidates[i])
            backtrack(i+1,curr+candidates[i])
            res.pop()

            while  i+1<len(candidates) and candidates[i]==candidates[i+1] :
                i+=1
            backtrack(i+1,curr)

        backtrack(0,0)
        return sol