class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,e in enumerate(nums):
            seen[e]=i
        for i,e in enumerate(nums):
            diff=target-e
            if diff in seen and seen[diff]!=i:
                return [i,seen[diff]]

        
