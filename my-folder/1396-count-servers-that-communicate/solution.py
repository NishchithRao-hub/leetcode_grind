class Solution:
    # Iteration method
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_count, col_count = [0] * rows, [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and max(row_count[r], col_count[c]) > 1:
                    result += 1

        return result

# Time -> O(m*n) (m=number of rows, n=number of cols)
# Space -> O(m+n)
        
