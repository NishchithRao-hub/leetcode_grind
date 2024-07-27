class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        o = "O"
        m = len(board)
        n = len(board[0])

        queue = deque()
        for i in range(m):
            if board[i][0] == o:
                queue.append((i,0))
            if board[i][n-1] == o:
                queue.append((i,n-1))
            
        for j in range(n):
            if board[0][j] == o:
                queue.append((0,j))
            if board[m-1][j] == o:
                queue.append((m-1,j))

        def inBounds(i,j):
            return (0 <= i < m) and (0 <= j < n)
        
        while queue:
            i,j = queue.popleft()
            board[i][j] = "*"

            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i, j-1)]:
                if not inBounds(x,y):
                    continue
                if board[x][y] != o:
                    continue
                queue.append((x,y))
                board[x][y] = "*"

        for i in range(m):
            for j in range(n):
                if board[i][j] == o:
                    board[i][j] = 'X'
                elif board[i][j] == "*":
                    board[i][j] = o        
