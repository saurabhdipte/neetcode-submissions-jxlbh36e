class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        l=0
        r=len(people)-1
        while l<=r:
            remwt=limit-people[r]
            boats+=1
            r-=1
            if remwt>=people[l]:
                l+=1
        return  boats       


