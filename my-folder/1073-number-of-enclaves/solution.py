class Solution:
    # Matrix BFS
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = [[False] * cols for _ in range(rows)]
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        land = 0
        for r in range(rows):
            for c in range(cols):
                land += grid[r][c]
                if (grid[r][c] == 1 and (r in [0, rows-1] or c in [0, cols-1])):
                    q.append((r, c))
                    visit[r][c] = True

        borderlands = 0
        while q:
            r, c = q.popleft()
            borderlands += 1
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1
                    and not visit[new_r][new_c]):
                    q.append((new_r, new_c))
                    visit[new_r][new_c] = True

        return land - borderlands

# Time -> O(m * n)
# Space -> O(m * n)
