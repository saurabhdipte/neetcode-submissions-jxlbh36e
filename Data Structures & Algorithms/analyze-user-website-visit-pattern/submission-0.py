from itertools import combinations
from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        adj=defaultdict(list)
        for (t,user,web) in sorted(zip(timestamp,username,website)):
            adj[user].append(web)

        score=defaultdict(int)
        for user,website in adj.items():
            for pattern in set(combinations(website,3)):
                score[pattern]+=1
        max_cnt,max_pattern=0,()
        for pattern,cnt in score.items():
            if cnt>max_cnt or (cnt==max_cnt and pattern<max_pattern):
                max_cnt=cnt
                max_pattern=pattern
        return list(max_pattern)