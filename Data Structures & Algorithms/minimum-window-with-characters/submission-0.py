class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen=collections.defaultdict(int)
        for char in t:
            seen[char]+=1
        formed,total=0,len(seen)
        l,r=0,0
        minlen=float("inf")
        subl,subr=0,0
        while r<len(s):
            char=s[r]
            if char in seen:
                seen[char]-=1
                if seen[char]==0:
                    formed+=1
            while formed==total and l<=r:
                curlen=r-l+1
                if curlen<minlen:
                    minlen=curlen
                    subl=l
                    subr=r+1
                char=s[l]
                if char in seen:
                    if seen[char]==0:
                        formed-=1
                    seen[char]+=1
                l+=1
            r+=1
        return "" if minlen==float("inf") else s[subl:subr]
        




            
            
