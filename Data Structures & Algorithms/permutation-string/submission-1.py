class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cache1=collections.defaultdict(int)
        cache2=collections.defaultdict(int)
        if len(s1)>len(s2): return False
        for i in range(len(s1)):
            cache1[s1[i]]+=1
            cache2[s2[i]]+=1
        if cache1==cache2: return True
        for i in range(len(s1),len(s2)):
            cache2[s2[i]] +=1
            cache2[s2[i-len(s1)]]-=1
            if cache2[s2[i-len(s1)]]==0:
                del cache2[s2[i-len(s1)]]
            if cache1==cache2:
                return True
        return False
