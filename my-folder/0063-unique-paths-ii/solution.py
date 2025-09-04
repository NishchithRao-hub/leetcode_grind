class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DP bottom-up approach
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        dp = [[0] * (COLS+1) for _ in range(ROWS+1)]

        dp[ROWS-1][COLS-1] = 1

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r+1][c]
                    dp[r][c] += dp[r][c+1]

        return dp[0][0] 

# Time -> O(ROWS * COLS)
# Space -> O(ROWS * COLS)
        
