class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(speed):
            total = 0
            for pile in piles:
                total += math.ceil(pile/speed)
            if total<=h:
                return True
            return False
        left,right=1,max(piles)
        while left<right:
            mid = left  + (right-left)//2
            if check(mid) == True:
                right = mid
            else:
                left = mid + 1
        return left