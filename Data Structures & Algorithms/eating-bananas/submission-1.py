class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/k)
            if hours<=h:
                return True
            else: return False
        l=1
        r=max(piles)
        while l<r:
            k=(l+r)//2
            if k_works(k) == True:
                r=k
            else:
                l=k+1
        return l