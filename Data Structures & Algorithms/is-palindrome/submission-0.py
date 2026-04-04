class Solution:
    def isPalindrome(self, s: str) -> bool:
        point1=0
        point2=len(s)-1
        while point1<point2:
            while point1<point2 and not s[point1].isalnum():
                point1+=1
            while point1<point2 and not s[point2].isalnum():
                point2-=1
            if s[point1].lower()!=s[point2].lower():
                return False
            point1+=1
            point2-=1
        return True
