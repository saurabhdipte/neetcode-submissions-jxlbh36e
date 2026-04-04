from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        adj=defaultdict(list)
        for (t,user,web) in sorted(zip(timestamp,username,website)):
            adj[user].append(web)
        scores=defaultdict(int)
        for user,website in adj.items():
            for pattern in set(combinations(website,3)):
                scores[pattern]+=1

        maxpattern=""
        maxcnt=0      
        for pattern,score in scores.items():
            if score>maxcnt or (score==maxcnt and pattern<maxpattern):
                maxcnt=score
                maxpattern=pattern
        return list(maxpattern)
