class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen=0
        left = 0

        def palindrome(s,l,r):
            nonlocal maxlen, left
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1>=maxlen):
                    maxlen=r-l+1
                    left=l
                l-=1
                r+=1    

        for i in range(len(s)):
            l,r=i,i
            palindrome(s,l,r)
            l,r=i,i+1
            palindrome(s,l,r)
        return s[left : (left + maxlen )]
    

              