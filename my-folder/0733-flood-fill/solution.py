class Solution:
    # BFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image

        max_r, max_c = len(image), len(image[0])
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < max_r and 0 <= nc < max_c and image[nr][nc] == original:
                    image[nr][nc] = color
                    queue.append((nr, nc))

        return image

# Time -> O(V*E)
# Space -> O(V*E)        
