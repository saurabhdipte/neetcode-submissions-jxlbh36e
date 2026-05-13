class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def cansplit(largest):
            cursum = 0
            subarrays = 1
            for num in nums:
                cursum += num
                if cursum>largest:
                    subarrays +=1
                    if subarrays>k:
                        return False
                    cursum = num
            return True
        left = max(nums)
        right = sum(nums)
        res = float('inf')
        while left <= right:
            mid = left + (right - left)//2
            if cansplit(mid) == True:
                res = mid
                right = mid -1 
            else:
                left = mid + 1
        return res
