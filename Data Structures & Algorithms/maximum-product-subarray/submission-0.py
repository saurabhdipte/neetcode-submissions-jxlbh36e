class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmin,curmax=1,1
        for num in nums:
            if num==0:
                curmin,curmax=1,1
                continue
            temp=num*curmax
            curmax=max(num*curmax,num*curmin,num)
            curmin=min(temp,num*curmin,num)
            res=max(res,curmax,curmin)
        return res

