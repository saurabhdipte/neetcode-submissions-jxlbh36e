class Twitter:

    def __init__(self):
        self.count=0
        self.followMap = collections.defaultdict(set) #userid to set of followers
        self.tweetMap = collections.defaultdict(list) #userid to list of tweetid
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1


    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        minheap=[]
        heapq.heapify(minheap)
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]  )-1
                count,tweetid = self.tweetMap[followeeId][index]
                heapq.heappush(minheap,[count,tweetid,followeeId,index-1])
        while minheap and len(res)<10:
            count,tweetid,followeeId,index=heapq.heappop(minheap)
            res.append(tweetid)
            if index>=0:
                count,tweetid=self.tweetMap[followeeId][index]
                heapq.heappush(minheap,[count,tweetid,followeeId,index-1])
        return res
                


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
