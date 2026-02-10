# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 0)]
        total_sum = 0

        while stack:
            node, curr_num = stack.pop()

            new_num = curr_num * 10 + node.val

            if not node.right and not node.left:
                total_sum += new_num
            else:
                if node.right:
                    stack.append((node.right, new_num))
                if node.left:
                    stack.append((node.left, new_num))
            
        return total_sum
            
        
