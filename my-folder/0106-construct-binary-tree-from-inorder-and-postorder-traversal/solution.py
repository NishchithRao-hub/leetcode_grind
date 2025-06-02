# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexes = {val: idx for idx, val in enumerate(inorder)}
        self.postorder_idx = len(postorder)-1

        def dfs(l, r):
            if l > r:
                return
            root_val = postorder[self.postorder_idx]
            self.postorder_idx -= 1
            root = TreeNode(root_val)

            mid = indexes[root_val]

            root.right = dfs(mid+1, r)
            root.left = dfs(l, mid-1)
            
            return root

        return dfs(0, len(inorder)-1)

        
        
