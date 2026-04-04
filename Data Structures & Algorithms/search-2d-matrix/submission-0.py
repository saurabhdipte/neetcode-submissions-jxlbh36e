class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        total=rows*cols
        l=0
        r=total-1
        while l<=r:
            m=(l+r)//2
            i,j=m//cols, m%cols
            midval=matrix[i][j]
            if midval==target:
                return True
            elif target>midval:
                l=m+1
            else:
                r=m-1
        return False
        