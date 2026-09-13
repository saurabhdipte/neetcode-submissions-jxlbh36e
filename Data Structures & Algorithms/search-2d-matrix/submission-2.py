class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        total = rows*cols
        left,right = 0, total-1
        while left<=right:
            mid = left + (right - left )//2
            i,j = mid//cols,mid%cols
            if matrix[i][j]<target:
                left = mid + 1
            elif matrix[i][j]>target:
                right = mid - 1
            else:
                return True
        return False