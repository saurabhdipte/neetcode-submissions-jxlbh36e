class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(m):
            current_capacity=0
            day=1
            for weight in weights:
                if current_capacity+weight>m:
                    day+=1
                    if day>days:
                        return False
                    current_capacity=0
                current_capacity+=weight
            return True



                 
        l=max(weights)
        r=sum(weights)
        while l<=r:
            m=l+ (r-l)//2
            if can_ship(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res