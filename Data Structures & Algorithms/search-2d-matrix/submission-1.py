class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        total=rows*cols
        l,r=0,total-1
        while l<=r:
            m=(l+r)//2
            i,j=m//cols,m%cols
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                r-=1
            else:
                l+=1
        return False
