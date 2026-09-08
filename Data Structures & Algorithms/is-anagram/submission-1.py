class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        seen1=collections.Counter(s)
        seen2=collections.Counter(t)
        if seen1==seen2:
            return True
        return False