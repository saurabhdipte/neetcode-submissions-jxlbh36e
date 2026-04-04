class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if i==j==0:
                    continue
                leftpath=uppath=float("inf")
                if i!=0:
                    uppath=grid[i][j] + grid[i-1][j]
                if j!=0:
                    leftpath=grid[i][j]+grid[i][j-1]
                grid[i][j]=min(leftpath,uppath)
        return grid[rows-1][cols-1]