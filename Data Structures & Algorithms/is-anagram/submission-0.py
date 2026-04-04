from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dicts=defaultdict(int)
        dictt=defaultdict(int)
        for char in s:
            dicts[char]+=1
        for char in t:
            dictt[char]+=1
        if (dicts==dictt):
            return True
        else: return False