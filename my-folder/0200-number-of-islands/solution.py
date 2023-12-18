class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        m = len(grid)
        n = len(grid[0])
        
        def dfs(a , b):
            grid[a][b] = -1
            if (a < m - 1 and grid[a+1][b] == "1"):
                dfs(a+1,b)
            if (a > 0 and grid[a-1][b] == "1"):
                dfs(a-1,b)
            if (b < n - 1 and grid[a][b+1] == "1"):
                dfs(a,b+1)
            if (b > 0 and grid[a][b-1] == "1"):
                dfs(a,b-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islandCount += 1
                    dfs(i,j)
        return islandCount


