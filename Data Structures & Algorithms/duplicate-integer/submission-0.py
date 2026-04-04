class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        inset = set()
        for num in nums:
            if num in inset:
                return True
            else:
                inset.add(num)
        return False