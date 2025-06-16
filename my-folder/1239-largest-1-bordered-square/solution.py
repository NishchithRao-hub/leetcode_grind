class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        up = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]

        # Precompute up and left arrays
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    up[i][j] = 1 + (up[i - 1][j] if i > 0 else 0)
                    left[i][j] = 1 + (left[i][j - 1] if j > 0 else 0)

        max_side = 0

        # Try all possible bottom-right corners (i, j)
        for i in range(m):
            for j in range(n):
                small = min(up[i][j], left[i][j])
                while small > 0:
                    if up[i][j - small + 1] >= small and left[i - small + 1][j] >= small:
                        max_side = max(max_side, small)
                        break
                    small -= 1

        return max_side * max_side

# Time & Space Complexity
# Time: O(m * n * min(m, n))
# For each cell, worst-case check all square sizes (but breaks early).
# Space: O(m * n) for up and left DP tables.
        
