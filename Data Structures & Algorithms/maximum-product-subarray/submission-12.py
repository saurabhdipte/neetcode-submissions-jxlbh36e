class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)  
        curmin=1
        curmax=1
        for num in nums:
            if num==0:
                curmin=1
                curmax=1
            temp1=num*curmin
            temp2=num*curmax
            curmin = min(temp1, temp2, num)
            curmax = max(temp2, temp1, num)

            res=max(curmin,curmax,res)
        return res