class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==0 or numRows>len(s):
            return s
        res=[[] for i in range(numRows)]
        row=0
        dir=1
        for char in s:
            res[row].append(char)
            row+=dir
            if row==0 or row==(numRows-1):
                dir*=-1
        result=""
        for ans in res:
            result+= "".join(ans)
        return result