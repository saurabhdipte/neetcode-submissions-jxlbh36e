class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        total=sum(nums)
        half=total//2
        seen=set()
        seen.add(0)
        for i in range(len(nums) -1 ,-1,-1):
            seendp=set()
            for t in seen:
                seendp.add(t+nums[i])
                seendp.add(t)
            seen=seendp
        if half in seen:
            return True
        return False