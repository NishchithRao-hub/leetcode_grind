# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.curr_idx = 0
        self.inorder(root)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        value = self.arr[self.curr_idx]
        self.curr_idx += 1
        return value        

    def hasNext(self) -> bool:
        return self.curr_idx <= len(self.arr) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
