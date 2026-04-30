class Solution:
    def totalNQueens(self, n: int) -> int:
        cols=set()
        pdiag=set()
        ndiag=set()
        count=0
        def backtrack(r):
            nonlocal count
            if r==n:
                count+=1
                return
            for c in range(n):
                if c in cols or r+c in pdiag or r-c in ndiag:
                    continue
                cols.add(c)
                pdiag.add(r+c)
                ndiag.add(r-c) 
                backtrack(r+1) 
                cols.remove(c)
                pdiag.remove(r+c)
                ndiag.remove(r-c) 
        backtrack(0)
        return count
