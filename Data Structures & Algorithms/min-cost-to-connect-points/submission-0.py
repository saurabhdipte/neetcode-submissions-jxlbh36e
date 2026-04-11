class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adj=collections.defaultdict(list)
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist=(abs(x2-x1) + abs(y2-y1))
                adj[i].append([dist, j])
                adj[j].append([dist,i])
        visit=set()
        minheap=[[0,0]]
        res=0
        while len(visit)!=n:
            cost,point=heapq.heappop(minheap)
            if point in visit:
                continue
            visit.add(point)
            res+=cost
            for neicost,nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minheap,[neicost,nei])
        return res

                