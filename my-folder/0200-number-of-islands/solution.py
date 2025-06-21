class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS Approach
        moves = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r_index, c_index):
            if (r_index < 0 or c_index < 0 or r_index >= rows or c_index >=
                cols or grid[r_index][c_index] == "0"):
                return

            grid[r_index][c_index] = "0"
            for dir_r, dir_c in moves:
                dfs(r_index + dir_r, c_index + dir_c)
            
        for r_index in range(rows):
            for c_index in range(cols):
                if grid[r_index][c_index] == "1":
                    dfs(r_index, c_index)
                    islands += 1
        return islands

# Time complexity = O(m*n)
# Space complexity = O(m*n)
# Where m is the number of rows and n is the number of columns in the grid.
        
