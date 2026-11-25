class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        q=collections.deque()
        visit=set()
        steps=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i,j))
                    visit.add((i,j))
        

        def addcell(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or (i,j) in visit or grid[i][j]==-1:
                return
            else:
                q.append((i,j))
                visit.add((i,j))
        
        while q:
            for i in range(len(q)):
                i,j=q.popleft()
                grid[i][j]=steps
                addcell(i+1,j)
                addcell(i-1,j)
                addcell(i,j+1)
                addcell(i,j-1)
            steps+=1

        