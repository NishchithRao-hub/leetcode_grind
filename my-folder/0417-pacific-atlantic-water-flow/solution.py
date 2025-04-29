class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific_visited = set()
        atlantic_visited = set()


        def dfs(visited, row, col, start):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if (row, col) in visited:
                return
            
            if heights[row][col] < start:
                return
            
            visited.add((row, col))

            dfs(visited, row+1, col, heights[row][col])
            dfs(visited, row-1, col, heights[row][col])
            dfs(visited, row, col+1, heights[row][col])
            dfs(visited, row, col-1, heights[row][col])

        for col in range(cols):
            dfs(pacific_visited, 0, col, heights[0][col]) #1st row
            dfs(atlantic_visited, rows-1, col, heights[rows-1][col]) #last row

        for row in range(rows):
            dfs(pacific_visited, row, 0, heights[row][0]) #1st col
            dfs(atlantic_visited, row, cols-1, heights[row][cols-1]) #last col

        result = [list(value) for value in pacific_visited & atlantic_visited]

        return result
