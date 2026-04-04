class Solution:
    def palindrome(self,s,l,r):
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res,sol=[],[]
        def backtrack(i):
            if i==len(s):
                sol.append(res[:])
                return
            for j in range(i,len(s)):
                if self.palindrome(s,i,j):
                    res.append(s[i:j+1])
                    backtrack(j+1)
                    res.pop()
        backtrack(0)
        return sol
            
        