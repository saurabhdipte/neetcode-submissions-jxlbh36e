class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        for index,element in enumerate(nums):
            if element in seen and index-seen[element]<=k:
                return True
            seen[element]=index
        return False