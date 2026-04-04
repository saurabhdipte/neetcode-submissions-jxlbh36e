class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen=Counter(nums)
        for key,value in seen.items():
            if value>(len(nums)/2):
                return key