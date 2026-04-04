class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row,dir=0,1
        res=[[] for i in range(numRows)]
        for char in s:
            res[row].append(char)
            row+=dir
            if row==0 or row==(numRows-1):
                dir*=-1
        result=""
        for ans in res:
            result+= "".join(ans)
        return result