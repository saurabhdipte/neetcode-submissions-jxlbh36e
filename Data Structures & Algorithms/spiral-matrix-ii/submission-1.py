class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0] * n for _ in range(n)]
        top,left=0,0
        bot,right=n,n
        count=1
        while left<right and top<bot:
            for i in range(left,right):
                res[top][i]=count
                count+=1
            top+=1
            for i in range(top,bot):
                res[i][right-1]=count
                count+=1
            right-=1
            if not (left<right and top<bot):
                break
            for i in range(right-1,left-1,-1):
                res[bot-1][i]=count
                count+=1
            bot-=1
            for i in range(bot-1,top-1,-1):
                res[i][left]=count
                count+=1
            left+=1

        return res