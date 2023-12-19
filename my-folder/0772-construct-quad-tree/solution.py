"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.helper(grid, 0, 0, len(grid))

    def allSame(self, grid, i, j, width):
        for a in range(i , i + width):
            for b in range(j, j + width):
                if grid[a][b] != grid[i][j]:
                    return False
        return True

    def helper(self, grid , i, j, width):
        if self.allSame(grid, i, j, width):
            return Node(grid[i][j] == 1, True)

        node = Node(True, False)
        node.topLeft = self.helper(grid, i, j, width // 2)
        node.topRight = self.helper(grid, i, j + width // 2, width // 2)
        node.bottomLeft = self.helper(grid, i + width // 2, j, width // 2)
        node.bottomRight = self.helper(grid, i + width // 2, j + width // 2, width // 2)
        return node

