class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        res = 0
        count=collections.defaultdict(int)
        for right in range(len(s)):
            count[s[right]]+=1
            while (right-left+1 - max(count.values()))>k:
                
                count[s[left]]-=1
                left+=1
            res = max(res,right-left+1)
            right+=1
        return res
