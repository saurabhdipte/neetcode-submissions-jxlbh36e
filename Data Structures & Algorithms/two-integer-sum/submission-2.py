class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,element in enumerate(nums):
            seen[element]=index
        for index,element in enumerate(nums):
            diff=target - element
            if diff in seen and index!=seen[diff]:
                return [index,seen[diff]]
            