class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        if rows==1 and cols==1:
            return board[0][0] ==word

        def backtrack(i,j,index):
            if len(word)== index:
                return True
            if board[i][j]!=word[index]:
                return False
            char=board[i][j]
            board[i][j]='#'
            for m,n in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                if 0<=m<rows and 0<=n<cols:
                    if backtrack(m,n,index+1):
                        return True
            board[i][j]=char
            return False


        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j,0):
                    return True
        return False
            