class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # DFS + BFS approach
        N = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if 0 <= r < N and 0 <= c < N and grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r, c))
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        q = deque()
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    break
            if q:
                break

        result = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] == 1:
                            return result
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))

            result += 1

# Time -> O(n^2)
# Space -> O(n^2)
        
