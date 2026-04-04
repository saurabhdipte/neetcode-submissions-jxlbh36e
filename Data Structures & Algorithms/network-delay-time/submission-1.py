class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append((w,v))
        minheap=[[0,k]]
        res={}
        while minheap:
            w1,n1 =heapq.heappop(minheap)
            if n1 in res:
                continue
            res[n1]=w1
            for w2,n2 in adj[n1]:
                if n2 not in res:
                    heapq.heappush(minheap,[w1+w2,n2])
        if len(res)!=n:
            return -1
        return max(res.values())