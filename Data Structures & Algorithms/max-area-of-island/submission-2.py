class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        maxarea=0
        visit=set()
        def dfs(i,j):
            if (i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==0 or (i,j) in visit):
                return 0
            else:
                visit.add((i,j))
                return (1+dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1))

        for i in range(rows):
            for j in range(cols):
                maxarea=max(maxarea,dfs(i,j))
        return maxarea
