# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Bottom-up Approach
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        dp = [[] for _ in range(n+1)]
        dp[1].append(TreeNode(0))

        for count in range(3, n+1, 2):
            for i in range(1, count-1, 2):
                j = count - i - 1
                for left in dp[i]:
                    for right in dp[j]:
                        root = TreeNode(0, left, right)
                        dp[count].append(root)
                    
        return dp[n]

# Time complexity: O(2^(n/2)) There are a maximum of 2^(n/2) possible full binary trees with n nodes (where n is an odd number) and the algorithm generates all of them without solving any subproblem twice. 
# Space complexity: O(n*(2n/2)). dp[i] will store the list of root nodes for all possible full binary trees with i nodes. As there can be a maximum of 2^(n/2)possible full binary trees with n nodes, dp will consume O(n*(2n/2)) space to store the list of nodes corresponding to all the number of nodes from 1 to n.
