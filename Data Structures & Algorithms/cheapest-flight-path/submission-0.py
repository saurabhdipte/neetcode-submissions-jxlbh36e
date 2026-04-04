class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res=[float("inf")]*n
        res[src]=0
        for i in range(k+1):
            rescopy=res.copy()
            for u,v,w in flights:
                if res[u]==float("inf"):
                    continue
                if res[u]+w<rescopy[v]:
                    rescopy[v]=res[u] + w
            res=rescopy
        return -1 if res[dst]==float("inf") else res[dst]