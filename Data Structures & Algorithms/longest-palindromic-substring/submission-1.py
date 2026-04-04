class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=[]
        def palindrome(s,l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                res.append(s[l:(r+1)])
                l-=1
                r+=1
        for i in range(len(s)):
            l,r=i,i
            palindrome(s,l,r)
            l,r=i,i+1
            palindrome(s,l,r)
        res.sort(key=len,reverse=True)
        return res[0]        