class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(l,r):
            while l<=r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        

        l=0
        r=len(s) - 1
        while l<=r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return palindrome(l,r-1) or palindrome(l+1,r)
        return True