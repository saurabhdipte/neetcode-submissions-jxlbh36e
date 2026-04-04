class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin = 1
        curmax = 1

        for num in nums:
            if num == 0:
                curmin, curmax = 1, 1
                continue

            temp = num * curmax
            temp2 = num * curmin

            curmax = max(num, temp, temp2)
            curmin = min(num, temp, temp2)

            res = max(res, curmax)

        return res