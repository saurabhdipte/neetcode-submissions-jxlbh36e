from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        pseen,aseen=set(),set()
        pq,aq=deque(),deque()


        for j in range(cols):
            pq.append((0,j))
            pseen.add((0,j))
        for i in range(1,rows):
            pq.append((i,0))
            pseen.add((i,0))

        for j in range(cols):
            aq.append((rows-1,j))
            aseen.add((rows-1,j))
        for i in range(rows-1):
            aq.append((i,cols-1))
            aseen.add((i,cols-1))

        def bfs(que,seen):
            while que:
                i,j=que.popleft()
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=r<rows and 0<=c<cols and (r,c) not in seen and heights[i][j]<=heights[r][c]:
                        seen.add((r,c))
                        que.append((r,c))

        bfs(pq,pseen)
        bfs(aq,aseen)
        return list(pseen.intersection(aseen))