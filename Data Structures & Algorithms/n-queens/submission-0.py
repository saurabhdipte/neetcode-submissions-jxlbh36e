class Solution:
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols=set()
        pdiag=set() # r+c would be constant
        ndiag=set() #r-c would be constant
        board=[["."]* n for _ in range(n)]
        ans=[]
        def backtrack(r):
            if r==n:
                
                ans.append(["".join(row) for row in board[:]])
                return
            for c in range(n):
                if c in cols or (r+c) in pdiag or (r-c) in ndiag:
                    continue
                cols.add(c)
                pdiag.add(r+c)
                ndiag.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)

                cols.remove(c)
                pdiag.remove(r+c)
                ndiag.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return ans
            
                