class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        # dp=[[0] * (cols+1) for _ in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
        for i in range(rows-2,-1,-1):
            for j in range(cols-2,-1,-1):
                if matrix[i][j]==1:
                    matrix[i][j]=1+min(matrix[i+1][j] , matrix[i][j+1],matrix[i+1][j+1])
        maxsquare=0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]>=maxsquare:
                    maxsquare=matrix[i][j]
        return maxsquare**2



    
