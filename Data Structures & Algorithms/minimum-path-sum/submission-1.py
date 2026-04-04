class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp=[float("inf") ] *( cols+1)
        dp[cols-1]=0
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                dp[j]=grid[i][j]+min(dp[j] , dp[j+1])
        return dp[0]