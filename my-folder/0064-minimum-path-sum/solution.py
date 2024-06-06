class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        a = len(grid)
        b = len(grid[0])

        for i in range(1, a):
            grid[i][0] += grid[i-1][0]
        for i in range(1, b):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, a):
            for j in range(1, b):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
        
