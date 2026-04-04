class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m=len(board),len(board[0])
        q=collections.deque()
        for i in range(n):
            if board[i][0] == 'O':
                q.append((i,0))
            if board[i][m-1] == 'O':
                q.append((i, m-1))
                
        for j in range(m):
            if board[0][j] == 'O':
                q.append((0,j))
            if board[n-1][j] == 'O':
                q.append((n-1, j))
        while q:
            i,j=q.popleft()
            board[i][j]="#"
            for row,col in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                if 0<=row<n and 0<=col<m and board[row][col]=='O':
                    board[row][col]="#"
                    q.append((row,col))
        for i in range(n):
            for j in range(m):
                if board[i][j]!="#":
                    board[i][j]='X'
        for i in range(n):
            for j in range(m):
                if board[i][j]=='#':
                    board[i][j]='O'

