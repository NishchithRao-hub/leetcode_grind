class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Bottom up DP
        rows, cols = len(grid), len(grid[0])
        dp = [[float("inf")] * (cols+1) for _ in range(rows+1)]
        dp[rows-1][cols] = 0

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])

        return dp[0][0]        

# Time -> O(m*n) (m=num of rows, n=num of cols)
# Space -> O(m*n)
        
