class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen={}
        for num in nums:
            seen[num]=1+seen.get(num,0)
        for key,values in seen.items():
            if values==1:
                return key
        