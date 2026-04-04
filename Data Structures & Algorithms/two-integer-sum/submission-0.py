class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(nums):
            seen[n]=i
        for i,n in enumerate(nums):
            diff=target - n
            if diff in seen and  seen[diff]!=i:
                return[i,seen[diff]]