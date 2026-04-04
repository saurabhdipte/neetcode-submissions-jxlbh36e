class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visit=set()
        q=collections.deque([(0,0,1)])
        direction=[(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while q:
            r,c,length=q.popleft()
            if r<0 or c<0 or r>=n or c>=n or grid[r][c]==1:
                continue
            if r==n-1 and c==n-1:
                return length
            for dr,dc in direction:
                i=r+dr
                j=c+dc
                while (i,j) not in visit:
                    visit.add((i,j))
                    q.append((i,j,length+1))
        return -1
