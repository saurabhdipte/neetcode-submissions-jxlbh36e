class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count={}
        for task in tasks:
            count[task]=1+count.get(task,0)
        maxheap=[ -value for value in count.values()]
        heapq.heapify(maxheap)
        time=0
        q=collections.deque()
        while q or maxheap:
            time+=1
            if maxheap:
                task= 1 + heapq.heappop(maxheap)
                if task<0:
                    q.append([task,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time