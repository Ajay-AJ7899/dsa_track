class Solution:
    def dfs(self,r,c,visited,rows,cols,board):
        #edge cases
        if r <0 or r>= rows or c<0 or c>= cols:
            return
        if visited[r][c]==1 or board[r][c]!="O":
            return
        visited[r][c]=1
        self.dfs(r+1,c,visited,rows,cols,board)
        self.dfs(r,c+1,visited,rows,cols,board)
        self.dfs(r-1,c,visited,rows,cols,board)
        self.dfs(r,c-1,visited,rows,cols,board)

    def solve(self, board: list[list[str]]) -> None:
        #here i am using dfs bez we are going one to next 
        rows = len(board)
        cols = len(board[0])
        visited = [[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c== 0 or r == rows -1 or c == cols -1:
                    if board[r][c]=='O' and visited[r][c]==0:
                        self.dfs(r,c,visited,rows,cols,board)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and visited[r][c]==0:
                    board[r][c]="X"
        