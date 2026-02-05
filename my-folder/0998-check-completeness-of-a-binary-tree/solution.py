# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        nullEncountered = False
        while q:
            node = q.popleft()
            if node:
                if nullEncountered:
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                nullEncountered = True

        return True

# Time -> O(n)
# Space -> O(n)
