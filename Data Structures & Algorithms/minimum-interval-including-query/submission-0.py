class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])
        
        minheap=[]
        res={}
        i=0

        for query in sorted(queries):
            while i<len(intervals) and  intervals[i][0]<=query :
                l,r = intervals[i]
                heapq.heappush(minheap,(r-l+1,r))
                i+=1
            while minheap and minheap[0][1]<query:
                heapq.heappop(minheap)
            res[query] = minheap[0][0] if minheap else -1
        return [res[query] for query in queries]




  