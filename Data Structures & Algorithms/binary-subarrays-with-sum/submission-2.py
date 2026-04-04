class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res=0
        cursum=0
        count=collections.defaultdict(int)
        count[0]=1
        for r in range(len(nums)):
            cursum+=nums[r]
            diff = cursum - goal
            if diff in count:
                res+=count[diff]
            count[cursum]+=1
        return res