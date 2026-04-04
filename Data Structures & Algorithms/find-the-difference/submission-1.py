class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor=0
        for i in range(len(s)):
            xor^=ord(s[i])
        for i in range(len(t)):
            xor^=ord(t[i])
        return chr(xor)