# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.output = []
        def traverse(node, height) :
            if not node: return 
            if len(self.output) == height :
                self.output.append([])
            self.output[height].append(node.val)
            traverse(node.left, height+1)
            traverse(node.right, height+1)
        traverse(root, 0)
        return self.output
        
