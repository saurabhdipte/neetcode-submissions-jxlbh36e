class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=collections.Counter(tasks)
        maxheap=[-value for key,value in count.items()]
        q=collections.deque()
        heapq.heapify(maxheap)
        time=0
        while q or maxheap:
            time+=1
            if maxheap:
                value=1 + heapq.heappop(maxheap)
                if value<0:
                    q.append([value,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time