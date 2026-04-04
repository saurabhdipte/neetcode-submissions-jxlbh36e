class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for index,element in enumerate(temperatures):
            while stack and stack[-1][0]<element:
                lelement,lindex=stack.pop()
                res[lindex]=index-lindex
            stack.append((element,index))
        return res