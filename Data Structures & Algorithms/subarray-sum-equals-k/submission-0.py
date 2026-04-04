class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=cursum=0
        cache={0:1}
        for num in nums:
            cursum+=num
            diff=cursum-k
            res+=cache.get(diff,0)
            cache[cursum]=1+cache.get(cursum,0)
        return res