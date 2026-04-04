class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols=len(matrix),len(matrix[0])
        row=set()
        col=set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(cols):
                matrix[i][j]=0
        for j in col:
            for i in range(rows):
                matrix[i][j]=0