class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count=collections.Counter(nums)
        res,sol=[],[]
        def backtrack():
            if len(res)==len(nums):
                sol.append(res[:])
                return
            for num in count:
                if count[num]>0:
                    
                    res.append(num)
                    count[num]-=1

                    backtrack()

                    res.pop()
                    count[num]+=1
        backtrack()
        return sol