class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips.sort(key = lambda t:t[1])
        # minHeap=[] #we will store the end time and the number of passengers
        # curPassenger=0
        # for t in trips:
        #     numPassenger,start,end=t
        #     while minHeap and minHeap[0][0]<=start:
        #         curPassenger-=minHeap[0][1]
        #         heapq.heappop(minHeap)

        #     curPassenger+=numPassenger
        #     if curPassenger>capacity:
        #         return False
        #     heapq.heappush(minHeap,[end,numPassenger])
        # return True


        res=[0]*1001
        for t in trips:
                numPassenger,start,end=t
                res[start]+=numPassenger
                res[end]-=numPassenger
        count=0
        for i in range(1001):
                count+=res[i]
                if count>capacity:
                        return False
        return True
        