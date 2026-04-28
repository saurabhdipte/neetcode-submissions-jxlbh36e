class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        rows,cols=len(boxGrid),len(boxGrid[0])
        for row in boxGrid:
            c=cols-1
            for i in range(cols -1 ,-1,-1):
                if row[i]=="#":
                    if i!=c:
                        row[c]="#"
                        row[i]='.'
                    c-=1
                elif row[i]=='*':
                    c=i-1 
        res=[[''] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                res[j][rows - 1 - i]=boxGrid[i][j]
        return res

