
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        num_fresh=0
        q=collections.deque()
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c]==1):
                    num_fresh+=1
                elif (grid[r][c]==2):
                    q.append((r,c))
        if num_fresh==0:
            return 0
        time=-1
        while q:
            qsize=len(q)
            time+=1
            for _ in range(qsize):
                i,j = q.popleft()
                for r,c in [(i,j+1),(i+1,j),(i-1,j),(i,j-1)]:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2  
                        num_fresh -= 1
                        q.append((r, c))
        if num_fresh!=0:
            return -1
        else:
            return time
        