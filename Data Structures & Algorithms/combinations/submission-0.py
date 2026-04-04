class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res,sol=[],[]
        arr=[n for n in range(1,n+1)]
        def backtrack(i):
            if len(res)==k:
                sol.append(res[:])
                return
            if i==len(arr):
                return
            res.append(arr[i])
            backtrack(i+1)
            res.pop()

            backtrack(i+1)

        backtrack(0)
        return sol