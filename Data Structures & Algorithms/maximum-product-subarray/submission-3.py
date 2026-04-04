class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmin,curmax=1,1
        for n in nums:
            tempmax=n*curmax
            tempmin=n*curmin
            curmax=max(tempmax,tempmin,n)
            curmin=min(tempmin,tempmax,n)
            
            res=max(res,curmax,curmin)
        return res