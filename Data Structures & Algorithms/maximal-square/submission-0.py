class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        dp=[[0] * (cols+1) for _ in range(rows+1)]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if matrix[i][j]=="1":
                    dp[i][j]=1+min(dp[i+1][j] , dp[i][j+1],dp[i+1][j+1])
        maxsquare=0
        for i in range(rows):
            for j in range(cols):
                if dp[i][j]>=maxsquare:
                    maxsquare=dp[i][j]
        return maxsquare**2



    
