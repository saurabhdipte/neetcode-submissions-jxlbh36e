class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxleft = [0] * n
        maxright = [0] * n
        total = [0] * n

        maxleft[0] = height[0]
        maxright[n - 1] = height[n - 1]
        for i in range(1,n):
            maxleft[i] = max(maxleft[i-1] , height[i])
        for i in range(n-2,-1,-1):
            maxright[i] = max(maxright[i+1] , height[i])
        for i in range(n):
            total[i] = min(maxright[i],maxleft[i]) - height[i]
        return sum(total)
        